from flask import Flask

from .main import generate_workout,stringify_workout
app = Flask(__name__)

@app.route('/')
def standard_workout():
    return stringify_workout(generate_workout(10))