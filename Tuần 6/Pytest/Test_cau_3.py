from issue.bai3 import lists_are_equal

def test_1():
    assert lists_are_equal([1, 2, 3], [1, 2, 3]) == True

def test_2():
    assert lists_are_equal([1, 2, 3], [1, 2, 4]) == False

def test_3():
    assert lists_are_equal([1, 2, 3], [1, 2, 3, 4]) == False

def test_4():
    assert lists_are_equal([1, 2, 3], [1, 2]) == False

def test_5():
    assert lists_are_equal([1, 2, 3], [1, 3, 2]) == False