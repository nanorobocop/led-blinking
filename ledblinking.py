#!/usr/bin/env python

import time
import random

def initialize(pins):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for p in pins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p, False)

def tail_blinking(n, tail, speed):
    state = [False for _ in range(n)]
    while True:
        for i in range(n):
            state[i] = True
            yield state
            time.sleep(speed)
            state[i-tail] = False
            yield state

def apply_state(pins, prev, curr):
    if prev == None:
        for i in range(len(curr)):
            GPIO.output(pins[i], curr[i])
        return
    for i in range(len(curr)):
        if prev[i] != curr[i]:
            GPIO.output(pins[i], curr[i])

if __name__ == "__main__":
    import RPi.GPIO as GPIO

    pins = [27, 22, 5, 6, 13, 19, 26, 16, 20]
    tail = 2

    initialize(pins)
    
    prev = None
    for curr in tail_blinking(len(pins), 2, 0.2):
        apply_state(pins, prev, curr)
