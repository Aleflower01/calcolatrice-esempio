from calculator import somma, sottrai, moltiplica


def test_somma():
    assert somma(2, 3) == 5


def test_sottrai():
    assert sottrai(5, 3) == 2


def test_moltiplica():
    assert moltiplica(2, 3) == 6
