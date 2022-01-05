from cs1robots import *
load_world("F:\pyton2.7\worlds/rain2.wld")
hubo = Robot(beepers = 10, avenue = 2, street = 6, orientation = "E")
hubo.set_trace("blue")
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def mark_and_move():    
    hubo.move()
    hubo.drop_beeper()
    turn_right()
    hubo.move()

def unmark_and_finish():
    hubo.pick_beeper()
    hubo.turn_left()

def close_and_move():
    if hubo.right_is_clear():
        hubo.drop_beeper()
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
        
def close_windows():
    while not hubo.on_beeper():
        close_and_move()

mark_and_move()
close_windows()
unmark_and_finish()



