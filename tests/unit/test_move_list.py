import pytest
from move_list import MoveList
from mock import patch

@pytest.fixture()
def ml():
    ml = MoveList()
    yield ml

def test_init(ml):
    assert type(ml) is MoveList

def test_retrieve_moves_default(ml):
    ml.retrieve_moves(move_list_url=None)
    assert len(ml.moves) == 151