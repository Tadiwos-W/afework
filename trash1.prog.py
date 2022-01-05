from cs1robots import *
load_world("./worlds/trash1.wld")
hubo = Robot()
hubo.set_pause(0.2)
hubo.set_trace("blue")

def move_and_collect():
    while hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
            
def turn_arround():
    hubo.turn_left()
    hubo.turn_left()
    
def move_back():
    while hubo.front_is_clear():
        hubo.move()
        
def turn_right():
    for i in range(3):
        hubo.turn_left()
        
def throw_trash():
    turn_right()
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
        
move_and_collect()
turn_arround()
move_back()
throw_trash()
turn_arround()
move_back()
hubo.turn_left()





