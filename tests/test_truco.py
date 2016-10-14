import pytest

from truco import cards, get_card_by_id, get_card_by_description, Round


def test_there_are_40_cards():
    assert len(cards) == 40


def test_get_card_by_id():
    assert get_card_by_id(5).description == "3 de Oro"
    assert get_card_by_id(39).description == "4 de Basto"
    with pytest.raises(Exception):
        get_card_by_id(56)


def test_get_card_by_description():
    assert get_card_by_description("3 de Oro").identifier == 5
    assert get_card_by_description("4 de Basto").identifier == 39
    with pytest.raises(Exception):
        get_card_by_description("8 de oro")


def test_mano_1():
    g = get_card_by_description
    r = Round([
        [g("Ancho de espada"), g("Ancho de basto"), g("6 de Oro")],
        [g("3 de Espada"), g("3 de Oro"), g("4 de Oro")],
    ])
    assert r.result() == 1


def test_mano_2():
    """Mano parda"""
    g = get_card_by_description
    r = Round([
        [g("3 de Oro"), g("5 de Oro"), g("6 de Oro")],
        [g("3 de Espada"), g("3 de Oro"), g("4 de Oro")],
    ])
    assert r.result() == -1


def test_mano_3():
    """Mano con todas empatadas"""
    g = get_card_by_description
    r = Round([
        [g("3 de Oro"), g("5 de Oro"), g("6 de Oro")],
        [g("3 de Espada"), g("5 de Basto"), g("6 de Oro")],
    ])
    assert r.result() == 1


def test_mano_4():
    """Mano con las dos primeras empatadas menos la 3era"""
    g = get_card_by_description
    r = Round([
        [g("3 de Oro"), g("5 de Oro"), g("6 de Oro")],
        [g("3 de Espada"), g("5 de Basto"), g("7 de Oro")],
    ])
    assert r.result() == -1
