from issue.bai14 import find_mean

def test_1():
    assert find_mean([1, 2, 3, 4, 5]) == 3.0

def test_2():
    assert find_mean([]) == 0

def test_3():
    assert find_mean([1.1, 2.2, 3.3, 4.4, 5.5]) == 3.3

def test_4():
    assert find_mean([6, 2, 4, 5, 3, 1]) == 3.5

def test_5():
    assert find_mean([-5.5, 10.5, 4.5, -7.5, 0.0]) == 0.4