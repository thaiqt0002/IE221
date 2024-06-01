from issue.bai2 import is_sorted_ascending

def test_1():
    assert is_sorted_ascending([1, 2, 3]) == True

def test_2():
    assert is_sorted_ascending([]) == True

def test_3():
    assert is_sorted_ascending([-1]) == True

def test_4():
    assert is_sorted_ascending([1, 1, 1]) == True

def test_5():
    assert is_sorted_ascending([1, 3, 2]) == False