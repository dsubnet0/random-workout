import argparse
import random

from move_list import MOVE_LIST


def generate_workout(number_of_rounds=1, quietable_only=False, keep_balanced=True, cardio_only=False):
    my_workout = []
    move_list = MOVE_LIST

    my_workout.append(random.choice([m['name'] for m in move_list if 'opener' in m and m['opener']]))

    while len(my_workout) < number_of_rounds:
        next_move = ''
        if quietable_only:
            next_move = random.choice([m['name'] for m in move_list if 'quietable' in m and m['quietable']])
        elif cardio_only:
            next_move = random.choice([m['name'] for m in move_list if 'cardio' in m and m['cardio']])
        else:
            next_move = random.choice([m['name'] for m in move_list])
        my_workout.append(next_move)
        if keep_balanced and len(my_workout)<number_of_rounds and next_move in [m['name'] for m in move_list if 'reversible' in m and m['reversible']]:
            my_workout.append('OPPOSITE ' + next_move)
    return my_workout

def stringify_workout(workout_array):
    return_string = ''
    i=1
    for m in workout_array:
        return_string += f'{i}: {m}\n'    
        i+=1
    return return_string


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--quietable', help='Quietable only', action='store_true')
    parser.add_argument('--cardio', help='Cardio only', action='store_true')
    args = parser.parse_args()

    NUMBER_OF_ROUNDS = 18
    KEEP_BALANCED = True
    my_workout = generate_workout(
                    number_of_rounds=NUMBER_OF_ROUNDS, 
                    quietable_only=args.quietable, 
                    keep_balanced=KEEP_BALANCED,
                    cardio_only=args.cardio)

    print(stringify_workout(my_workout))
