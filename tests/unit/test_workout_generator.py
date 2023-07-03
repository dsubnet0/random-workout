import pytest
from workout_generator import WorkoutGenerator
from mock import patch


@pytest.fixture()
def wg():
    wg = WorkoutGenerator()
    yield wg


def test_init(wg):
    assert type(wg) is WorkoutGenerator


@patch('workout_generator.MoveList')
def test_generate_workout(mock_movelist, wg):
    mock_movelist.moves = [{'name': 'move1', 'opener': 1}]
    w = wg.generate_workout(mock_movelist)
    assert w == ['move1']


@patch('workout_generator.MoveList')
def test_generate_workout_cardio(mock_movelist, wg):
    mock_movelist.moves = [
        {'name': 'move1', 'opener': 1},
        {'name': 'move2', 'cardio': 1},
        {'name': 'move3'}
    ]
    w = wg.generate_workout(
        move_list=mock_movelist,
        cardio_only=True,
        number_of_rounds=2)
    assert w == ['move1', 'move2']


def test_random_choice_by_attribute(wg):
    moves = [{'name': 'move1', 'opener': 1}]
    assert wg._random_choice_by_attribute('opener', moves, 1) == 'move1'


def test_random_choice_by_attribute_empty(wg):
    moves = []
    assert wg._random_choice_by_attribute('opener', moves, 1) == ''
