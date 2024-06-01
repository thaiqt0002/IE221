from issue.bai5 import file_exists

def test_1():
    assert file_exists("issue", "bai0.py") == False

def test_2():
    assert file_exists("issue", "bai1.py") == True

def test_3():
    assert file_exists("issue", "bai2.c") == False

def test_4():
    assert file_exists("*", "test3.py") == False

def test_5():
    assert file_exists("test", "*") == False

