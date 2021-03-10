#!/usr/bin/env python

import ledblinking

def test_tail_blinking():
    g = ledblinking.circle_blinking(4, 2, 0)
    assert next(g) == [True, False, False, False]
    assert next(g) == [True, False, False, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, True, True, False]
    assert next(g) == [False, True, True, False]
    assert next(g) == [False, True, True, True]
    assert next(g) == [False, False, True, True]
    assert next(g) == [True, False, True, True]
    assert next(g) == [True, False, False, True]
    assert next(g) == [True, True, False, True]
    assert next(g) == [True, True, False, False]

def test_go_and_back():
    g = ledblinking.go_and_back(4, 2, 0)
    # go
    assert next(g) == [True, False, False, False]
    assert next(g) == [True, False, False, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, True, True, False]
    assert next(g) == [False, True, True, False]
    assert next(g) == [False, True, True, True]
    assert next(g) == [False, False, True, True]
    assert next(g) == [False, False, True, True]
    assert next(g) == [False, False, False, True]
    assert next(g) == [False, False, False, True]
    assert next(g) == [False, False, False, False]
    # back
    assert next(g) == [False, False, False, True]
    assert next(g) == [False, False, False, True]
    assert next(g) == [False, False, True, True]
    assert next(g) == [False, False, True, True]
    assert next(g) == [False, True, True, True]
    assert next(g) == [False, True, True, False]
    assert next(g) == [True, True, True, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, True, False, False]
    assert next(g) == [True, False, False, False]
    assert next(g) == [True, False, False, False]
    assert next(g) == [False, False, False, False]

def test_go_and_back_2():
    g = ledblinking.go_and_back_2(4, 1, 0)
    assert next(g) == [True, False, False, True]
    assert next(g) == [True, False, False, True]
    assert next(g) == [True, True, True, True]
    assert next(g) == [False, True, True, False]
    assert next(g) == [False, True, True, False]
    assert next(g) == [False, True, True, False]
    assert next(g) == [True, True, True, True]
    assert next(g) == [True, False, False, True]
    assert next(g) == [True, False, False, True]
    assert next(g) == [False, False, False, False]
