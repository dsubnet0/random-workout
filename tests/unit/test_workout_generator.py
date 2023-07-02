from workout_generator import WorkoutGenerator
from mock import patch


def test_init():
    wg = WorkoutGenerator()
    assert type(wg) is WorkoutGenerator


@patch('workout_generator.MoveList')
def test_generate_workout(mock_movelist):
    mock_movelist.moves = [{'name': 'move1', 'opener': 1}]
    wg = WorkoutGenerator()
    w = wg.generate_workout(mock_movelist)
    assert w == ['move1']
