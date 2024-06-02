from issue.bai4 import is_palindrome

def test_1():
    assert is_palindrome("racecar") == True

def test_2():
    assert is_palindrome("hello") == False

def test_3():
    assert is_palindrome("a") == True

def test_4():
    assert is_palindrome("ab") == False

def test_5():
    assert is_palindrome("") == True