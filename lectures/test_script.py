from script import func

def test_func():
    assert func(-3) == 3
    assert func(5) == 5
    assert func(0) == 0
