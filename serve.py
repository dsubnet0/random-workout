import os
from flask import Flask, render_template

from main import generate_workout,stringify_workout
app = Flask('Doug''s Workout Generator')

@app.route('/')
def standard_workout():
    return stringify_workout(generate_workout(10))

@app.route('/workout')
def formatted_workout(workout_array=None):
    return render_template('workout.html', workout_array=generate_workout(18))

app.run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)), debug=True)