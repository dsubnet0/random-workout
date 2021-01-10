import argparse
import json
import os
import random

parser = argparse.ArgumentParser()
parser.add_argument('--quietable', help='Quietable only', action='store_true')
args = parser.parse_args()

NUMBER_OF_ROUNDS = 18
KEEP_BALANCED = True
my_workout = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'move_list.json')) as move_json:
    move_data = json.load(move_json)
    move_list = move_data['move_list']

    my_workout.append(random.choice([m['name'] for m in move_list if 'opener' in m and m['opener']]))

    while len(my_workout) < NUMBER_OF_ROUNDS:
        next_move = ''
        if args.quietable:
            next_move = random.choice([m['name'] for m in move_list if 'quietable' in m and m['quietable']])
        else:
            next_move = random.choice([m['name'] for m in move_list])
        my_workout.append(next_move)
        if KEEP_BALANCED and next_move in [m['name'] for m in move_list if 'reversible' in m and m['reversible']]:
            my_workout.append('OPPOSITE ' + next_move)

for m in my_workout:
    print(m)