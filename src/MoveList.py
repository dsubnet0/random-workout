import json
import os
import random

import requests


class MoveList():

    def __init__(self, move_list_url: str = None):
        self.get_moves(move_list_url)
    

    def get_moves(self, move_list_url):
        if move_list_url:
            print(f'Getting move list from {move_list_url}')
            headers = {'user-agent': 'Wget/1.16 (linux-gnu)'}
            web_result = requests.get(move_list_url, stream=True, headers=headers)
            with open('download.file', 'wb+') as f:
                for chunk in web_result.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            with open('download.file', 'r') as f:
                file_contents = f.read()
                self.moves = json.loads(file_contents)
            os.remove('download.file')
        else:
            print(f'Using default move list')
            with open('default_move_list.json', 'r') as f:
                file_contents = f.read()
                self.moves = json.loads(file_contents)

    
    def generate_workout(self, number_of_rounds=1, keep_balanced=True, cardio_only=False, ppl=None):
        my_workout = []

        my_workout.append(random.choice([m['name'] for m in self.moves if 'opener' in m and m['opener']]))

        while len(my_workout) < number_of_rounds:
            next_move = ''
            if cardio_only:
                print(f'Cardio-only mode')
                next_move = random.choice([m['name'] for m in self.moves if 'cardio' in m and m['cardio']])
            elif ppl is not None:
                print(f'{ppl} mode')
                next_move = random.choice([m['name'] for m in self.moves if 'ppl' in m and m['ppl'] == ppl])
            else:
                next_move = random.choice([m['name'] for m in self.moves])
            my_workout.append(next_move)
            if (keep_balanced 
                and len(my_workout)<number_of_rounds 
                and next_move in [m['name'] for m in self.moves if 'reversible' in m and m['reversible']]
            ):
                my_workout.append('OPPOSITE ' + next_move)
        return my_workout


if __name__ == '__main__':
    # m = MoveList('https://www.dropbox.com/s/t928d8aroqxhfh9/move_list.json?dl=0')
    m = MoveList()
    print(m.moves)