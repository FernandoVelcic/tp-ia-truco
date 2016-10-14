from truco import get_card_by_id, Round
from training import round_as_training_set


def test_round_as_training_set():
    g = get_card_by_id
    r = Round([
        [g(2), g(9), g(25)],
        [g(8), g(0), g(36)],
    ])
    assert round_as_training_set(r) == \
        [
            -1, 0, 1, 0, 0, 0, 0, 0, -1, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, -1, 0, 0, 0
        ]
