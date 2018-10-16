import pytest

import hashtable


def test_get():
    h = hashtable.HashTable(5)
    h.put("test", 5)
    assert h.get("test") == 5

def test_is_empty():
    h = hashtable.HashTable(5)
    assert h.is_empty() is True

def test_size():
    h = hashtable.HashTable(5)
    h.put("test1", 1)
    h.put("test2", 2)
    h.put("test3", 3)
    h.put("test4", 4)
    assert h.size() == 4

def test_more_lists():
    h = hashtable.HashTable(50)
    h.put("thisisatest", 43242)
    h.put("another_test", 234)
    assert h.get("another_test") == 234
