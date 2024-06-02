from issue.bai7 import cubic_volume

def test_1():
    assert cubic_volume(1) == 1

def test_2():
    assert cubic_volume(2) == 8

def test_3():
    assert cubic_volume(0) == 0

def test_4():
    assert cubic_volume(-1) == -1

def test_5():
    assert cubic_volume(1.5) == 3.375