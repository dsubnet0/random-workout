import random
from typing import List

from move_list import MoveList


class WorkoutGenerator():
    def __init__(self) -> None:
        pass

    def generate_workout(self, 
                         move_list: MoveList, 
                         number_of_rounds: int = 1, 
                         keep_balanced: bool = True,
                         cardio_only: bool = False, 
                         ppl: bool = None
                         ) -> List:
        pass
        my_workout = []
        my_workout.append(random.choice(
                [ m['name'] for m in move_list.moves if 'opener' in m and m['opener'] ]
            )
        )

        while len(my_workout) < number_of_rounds:
            next_move = ''
            if cardio_only:
                print(f'Cardio-only mode')
                next_move = random.choice(
                    [ m['name'] for m in move_list.moves if 'cardio' in m and m['cardio'] ]
                )
            elif ppl is not None:
                print(f'{ppl} mode')
                next_move = random.choice(
                    [ m['name'] for m in move_list.moves if 'ppl' in m and m['ppl'] == ppl ]
                )
            else:
                next_move = random.choice([m['name'] for m in move_list.moves])
            my_workout.append(next_move)
            if (keep_balanced 
                and len(my_workout)<number_of_rounds 
                and next_move in [m['name'] for m in move_list.moves if 'reversible' in m and m['reversible']]
            ):
                my_workout.append('OPPOSITE ' + next_move)
        return my_workout

    
    def stringify_workout(self, workout_array):
        return_string = ''
        i=1
        for m in workout_array:
            return_string += f'{i}: {m}\n'    
            i+=1
        return return_string