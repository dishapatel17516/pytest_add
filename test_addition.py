from addition import calculate_add

def test_calculate_positive():
    assert calculate_add(10,20) == 30

def test_calculate_zero():
    assert calculate_add(0,15) == 15

def test_calculate_negative():
    assert calculate_add(-10,20) == 10       