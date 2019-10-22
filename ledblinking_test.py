#!/usr/bin/env python

import ledblinking

def test_tail_blinking():
    g = ledblinking.tail_blinking(4, 2, 0)
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
