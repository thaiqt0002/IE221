from issue.bai6 import calc_area

def test_1():
    assert calc_area(5) == 78.54

def test_2():
    assert calc_area(0) == 0.0

def test_3():
    assert calc_area(-1) == 3.14

def test_4():
    assert calc_area(5.5) == 95.03

def test_5():
    assert calc_area(-1.0) == 3.14