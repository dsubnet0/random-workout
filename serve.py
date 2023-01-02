import os

from flask import Flask, render_template, request

from main import generate_workout, stringify_workout

current_dir = os.path.dirname(__file__)
template_folder = os.path.join(current_dir, 'templates')
app = Flask('Doug''s Workout Generator', template_folder=template_folder)

@app.route('/raw')
@app.route('/raw/<int:number_of_rounds>')
def standard_workout(number_of_rounds=18):
    return stringify_workout(generate_workout(number_of_rounds))

@app.route('/workout')
@app.route('/workout/<int:number_of_rounds>')
def formatted_workout(number_of_rounds=18):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(number_of_rounds)
    )

@app.route('/quietworkout')
@app.route('/quietworkout/<int:number_of_rounds>')
def formatted_quiet_workout(number_of_rounds=18):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(number_of_rounds, quietable_only=True)
    )

@app.route('/cardio')
@app.route('/cardio/<int:number_of_rounds>')
def formatted_cardio_workout(number_of_rounds=18):
    return render_template(
            'workout.html', 
            workout_array=generate_workout(number_of_rounds, cardio_only=True)
    )

@app.route('/addmove', methods=['GET, POST'])
def add_move():
    if request.method == 'GET':
        return render_template(
            'addmove.html'
            ) 
    else:
        userdata = dict(request.form)
        move_name = userdata['move_name']
        is_opener = userdata['is_opener']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
