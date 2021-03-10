#!/usr/bin/env python

import time
import random
import os

def initialize(pins):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for p in pins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p, False)

def circle_blinking(n, tail, speed):
    state = [False for _ in range(n)]
    while True:
        for i in range(n):
            state[i] = True
            yield state
            time.sleep(speed)
            state[i-tail] = False
            yield state
            time.sleep(0.1 * speed)

def go_and_back(n, tail, speed):
    state = [False for _ in range(n)]
    while True:
        for i in range(n+tail):
            if i < n:
                state[i] = True
            yield state
            time.sleep(speed)
            if i-tail >= 0:
                state[i-tail] = False
            yield state
            time.sleep(0.1 * speed)
        time.sleep(speed)
        for i in range(n+tail):
            if i < n:
                state[-1 - i] = True
            yield state
            time.sleep(speed)
            if i-tail >= 0:
                state[-1 - (i-tail)] = False
            yield state
            time.sleep(0.1 * speed)
        time.sleep(speed)


def go_and_back_2(n, tail, speed):

    snake = go_and_back(n, tail, speed)

    for s in snake:
        state = [False for _ in range(n)]
        # import pdb; pdb.set_trace()
        for i in range(len(state)):
            # print(i, s[i])
            if s[i] == True:
                state[i] = True
                state[-1-i] = True
        yield state
        


def apply_state(pins, prev, curr):
    if prev == None:
        for i in range(len(curr)):
            GPIO.output(pins[i], curr[i])
        return
    for i in range(len(curr)):
        if prev[i] != curr[i]:
            GPIO.output(pins[i], curr[i])

def console_draw(state):
    os.write(1, "\r")
    for s in state:
        if s:
            os.write(1, "*")
        else:
            os.write(1, " ")

if __name__ == "__main__":
    try:
        import RPi.GPIO as GPIO
        gpio = True
    except ImportError:
        print("Failed to import RPi.GPIO; emulating only..")
        gpio = False

    pins = [27, 22, 5, 6, 13, 19, 26, 16, 20]
    tail = 2

    if gpio:
        initialize(pins)
    
    prev = None
    for curr in go_and_back_2(len(pins), tail, 0.1):
        if gpio:
            apply_state(pins, prev, curr)
        console_draw(curr)
