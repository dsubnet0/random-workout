import os

from flask import Flask, render_template

from move_list import MoveList
from workout_generator import WorkoutGenerator


current_dir = os.path.dirname(__file__)
template_folder = os.path.join(current_dir, '../templates')
move_list_file_url = 'https://www.dropbox.com/s/t928d8aroqxhfh9/move_list.json?dl=0'
app = Flask('Doug''s Workout Generator', template_folder=template_folder)
my_move_list = MoveList(move_list_file_url)
wg = WorkoutGenerator()


@app.route('/raw')
@app.route('/raw/<int:number_of_rounds>')
def standard_workout(number_of_rounds=18):
    return wg.stringify_workout(
            wg.generate_workout(
                move_list=my_move_list,
                number_of_rounds=number_of_rounds
            )
        )


@app.route('/workout')
@app.route('/workout/<int:number_of_rounds>')
def formatted_workout(number_of_rounds=18):
    return render_template(
            'workout.html',
            workout_array=wg.generate_workout(
                            move_list=my_move_list,
                            number_of_rounds=number_of_rounds
                        )
    )


@app.route('/cardio')
@app.route('/cardio/<int:number_of_rounds>')
def formatted_cardio_workout(number_of_rounds=18):
    return render_template(
            'workout.html',
            workout_array=wg.generate_workout(
                            move_list=my_move_list,
                            number_of_rounds=number_of_rounds,
                            cardio_only=True
                        )
    )


@app.route('/ppl/<ppl>')
@app.route('/ppl/<ppl>/<int:number_of_rounds>')
def formatted_push_workout(ppl, number_of_rounds=6):
    return render_template(
            'workout.html',
            workout_array=wg.generate_workout(
                            move_list=my_move_list,
                            number_of_rounds=number_of_rounds,
                            ppl=ppl
                        )
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
