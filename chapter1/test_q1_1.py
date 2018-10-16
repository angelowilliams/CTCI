import pytest
import q1_1

def test_1():
    assert q1_1.has_unique_chars("abcdefgh") is True

def test_2():
    assert q1_1.has_unique_chars("aa") is False

def test_3():
    assert q1_1.has_unique_chars("sfkjdsaf") is False

def test_4():
    assert q1_1.has_unique_chars("aaaaaaaaaaaaaaaaaaaaa") is False

def test_5():
    assert q1_1.has_unique_chars("the quick brown") is True

def test_6():
    assert q1_1.has_unique_chars("theq quick brown") is False
