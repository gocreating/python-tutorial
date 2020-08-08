import my_math

def test_add():
    assert my_math.add(1, 2) == 3
    assert my_math.add(99, 1) == 100

def test_minus():
    assert my_math.minus(5, 0) == 5
    assert my_math.minus(-2, 7) == -9
