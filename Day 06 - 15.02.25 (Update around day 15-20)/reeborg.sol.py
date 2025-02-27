# Reeborg Hurdle 4 ---> 1 Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while right_is_clear() == False:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while at_goal() == False:    
    if wall_in_front():
        jump()
    else:
        move()

# Maze Solution NON-DEBUGGED!!!
def turn_right():
    turn_left()
    turn_left()
    turn_left()
i = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():   
        move()
    else:
        turn_left()

        