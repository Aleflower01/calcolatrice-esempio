from calculator import somma, moltiplica


def test_somma():
    assert somma(2, 3) == 5


def test_moltiplica():
    assert moltiplica(2, 3) == 6
