from cs1robots import *
load_world("c:/python27/worlds/trash1.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()


def move_forward():
    while hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
def move_back():
    while hubo.front_is_clear():
        hubo.move()
    if not hubo.front_is_clear():
        turn_right()
        hubo.move()

def drop_trash():
    while hubo.carries_beepers():
        hubo.drop_beeper()
    turn_around()
    hubo.move()
    hubo.turn_left()
move_forward()
turn_around()
move_back()
drop_trash()
