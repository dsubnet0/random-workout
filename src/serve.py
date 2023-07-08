import os

from flask import Flask, render_template

from move_list import MoveList
from workout_generator import WorkoutGenerator
from ..cfg.dougs_settings import MOVE_LIST_FILE_URL


current_dir = os.path.dirname(__file__)
template_folder = os.path.join(current_dir, '../templates')

app = Flask('Doug''s Workout Generator', template_folder=template_folder)
if 'RANDOM_WORKOUT_APPLICATION' in os.environ:
    app.config.from_envvar('RANDOM_WORKOUT_APPLICATION_SETTINGS')
else:
    app.config['MOVE_LIST_FILE_URL'] = MOVE_LIST_FILE_URL
wg = WorkoutGenerator()


@app.route('/raw')
@app.route('/raw/<int:number_of_rounds>')
def standard_workout(number_of_rounds=18):
    my_move_list = MoveList(app.config['MOVE_LIST_FILE_URL'])
    return wg.stringify_workout(
            wg.generate_workout(
                move_list=my_move_list,
                number_of_rounds=number_of_rounds
            )
        )


@app.route('/workout')
@app.route('/workout/<int:number_of_rounds>')
def formatted_workout(number_of_rounds=18):
    my_move_list = MoveList(app.config['MOVE_LIST_FILE_URL'])
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
    my_move_list = MoveList(app.config['MOVE_LIST_FILE_URL'])
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
    my_move_list = MoveList(app.config['MOVE_LIST_FILE_URL'])
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
