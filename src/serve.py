import os

from flask import Flask, render_template

from main import generate_workout, stringify_workout

current_dir = os.path.dirname(__file__)
template_folder = os.path.join(current_dir, '../templates')
# template_folder = '../templates'
move_list_file_url = 'https://www.dropbox.com/s/t928d8aroqxhfh9/move_list.json?dl=0'
app = Flask('Doug''s Workout Generator', template_folder=template_folder)

@app.route('/raw')
@app.route('/raw/<int:number_of_rounds>')
def standard_workout(number_of_rounds=18):
    return stringify_workout(
            generate_workout(
                number_of_rounds, 
                move_list_url=move_list_file_url
            )
        )

@app.route('/workout')
@app.route('/workout/<int:number_of_rounds>')
def formatted_workout(number_of_rounds=18):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(
                            number_of_rounds, 
                            move_list_url=move_list_file_url
                        )
    )

@app.route('/cardio')
@app.route('/cardio/<int:number_of_rounds>')
def formatted_cardio_workout(number_of_rounds=18):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(
                            number_of_rounds, 
                            cardio_only=True, 
                            move_list_url=move_list_file_url
                        )
    )

@app.route('/push')
@app.route('/push/<int:number_of_rounds>')
def formatted_push_workout(number_of_rounds=6):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(
                            number_of_rounds, 
                            move_list_url=move_list_file_url,
                            ppl='push'
                        )
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
