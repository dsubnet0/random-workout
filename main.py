import argparse

from MoveList import MoveList


def generate_workout(number_of_rounds=1, cardio_only=False, move_list_url=None):
    my_move_list = MoveList(move_list_url)
    return my_move_list.generate_workout( number_of_rounds=number_of_rounds, cardio_only=cardio_only)


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
    my_workout = generate_workout(
                    number_of_rounds=NUMBER_OF_ROUNDS, 
                    cardio_only=args.cardio)

    print(stringify_workout(my_workout))
