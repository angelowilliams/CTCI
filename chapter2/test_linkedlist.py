import pytest

import linkedlist


def test_init():
    l = linkedlist.LinkedList()
    assert isinstance(l, linkedlist.LinkedList)

def test_add():
    l = linkedlist.LinkedList()
    node = l.add(5)
    assert isinstance(node, linkedlist.Node)

def test_remove_base_node_success():
    l = linkedlist.LinkedList()
    l.add(3)
    assert l.remove(3) == 0

def test_remove_last_node_success():
    l = linkedlist.LinkedList()
    l.add(2)
    l.add(1)
    assert l.remove(1) == 0

def test_remove_middle_node_success():
    l = linkedlist.LinkedList()
    l.add(10)
    l.add(20)
    l.add(30)
    assert l.remove(20) == 0

def test_remove_fail():
    l = linkedlist.LinkedList()
    l.add(50)
    assert l.remove(20) == -1

def test_find_success():
    l = linkedlist.LinkedList()
    l.add(234)
    assert isinstance(l.find(234), linkedlist.Node)

def test_find_fail():
    l = linkedlist.LinkedList()
    l.add(235)
    assert l.find(123) == -1

def test_size():
    l = linkedlist.LinkedList()
    l.add(100)
    l.add(1)
    l.add(43)
    assert l.size() == 3

def test_is_empty_success():
    l = linkedlist.LinkedList()
    assert l.is_empty()

def test_is_empty_fail():
    l = linkedlist.LinkedList()
    l.add(0)
    assert not l.is_empty()
