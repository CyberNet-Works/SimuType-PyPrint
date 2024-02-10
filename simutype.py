import random
import sys
import time
import string

def type_simulation(text, base_delay=0.005, glitch_factor=0.00025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in string.punctuation:
            if char in [',', '-', ':', ';', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', '`', '"', "'"]:
                shorter_pause = random.uniform(0.0025, 0.025)
                time.sleep(shorter_pause)
            else:
                longer_pause = random.uniform(0.025, 0.125)
                time.sleep(longer_pause)
        else:
            delay = max(0, base_delay + random.uniform(-glitch_factor, glitch_factor))
            time.sleep(delay)

def pyprint(*args, delay=0.0025, end='\n', sep=' '):
    for arg in args:
        if isinstance(arg, str):
            type_simulation(arg, delay)
        else:
            type_simulation(str(arg), delay)

    sys.stdout.write(end)
    sys.stdout.flush()
    time.sleep(max(0, delay))
