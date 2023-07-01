import argparse

from move_list import MoveList
from workout_generator import WorkoutGenerator


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--quietable', help='Quietable only', action='store_true')
    parser.add_argument('--cardio', help='Cardio only', action='store_true')
    args = parser.parse_args()

    number_of_rounds = 18
    my_move_list = MoveList()
    my_workout_generator = WorkoutGenerator()
    my_workout = my_workout_generator.generate_workout(
                    move_list=my_move_list,
                    number_of_rounds=number_of_rounds, 
                    cardio_only=args.cardio)

    print(my_workout_generator.stringify_workout(my_workout))
