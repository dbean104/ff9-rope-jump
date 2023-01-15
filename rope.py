from pynput.keyboard import Key, Controller
import time

# The player should be positioned with the exclamation mark
# above his/her head before starting this program.

# Time delay in seconds to allow the user to start this script
# and then make the PlayStation Remote Play window active
start_delay = 1

# Latency time, which may need to be adjusted
# with trial and error to compensate for connection latency
latency = 0.761

# Constants to define the jump intervals 
# throughout the various stages of the game
a = 0.667
b = 0.532
c = 0.466
d = 0.434
e = 0.383
g = 0.400
g2 = 0.401

delay = 0.1
currentInterval = a
extraTime = 0
balancer = 0
start = 0

def enter(delay):
    keyboard.press(Key.enter)
    time.sleep(delay)
    keyboard.release(Key.enter)

def wait(i):
    global currentInterval
    global balancer
    global delay
    global extraTime

    timer = (time.time() - start)
    if i == 1:
        currentInterval = a
    elif i == 21:
        currentInterval = b
        balancer = 0
    elif i == 51:
        currentInterval = c
        balancer = 0
    elif i == 101:
        currentInterval = d
        balancer = 0
    elif i == 201:
        currentInterval = e
        delay = 0.07
        balancer = 0
    elif i == 260:
        extraTime = 0.02
        balancer = 0
    elif i == 301:
        currentInterval = g
        balancer = 0
    elif i == 500 or i == 800:
        currentInterval = g2
    elif i == 600 or i == 900:
        currentInterval = g
    if i > 1:
        sleep_time = currentInterval - timer + balancer + extraTime
        time.sleep(sleep_time)

def input_jump(i):
    global start
    global balancer
    global extraTime
    full_time = time.time() - start - extraTime
    start = time.time()
    if i > 1:
        balancer += currentInterval - full_time
    enter(delay)
    extraTime = 0



keyboard = Controller()

# Delay to make the PlayStation Remote Play window active
time.sleep(start_delay)

# try to start the game
print('Starting game')
enter(delay)
time.sleep(2)
# accept
print('Accepting game')
enter(delay)
time.sleep(2)

# initiating first jump
print('Initiating first jump')
enter(delay)
time.sleep(latency)
for i in range(1,1005) :
    wait(i)
    input_jump(i)
    
