# Day 6: Functions, Code Block, Indentation, While Loop

## Reeborg's World

Probably the best way of learning python functions and how to define your own! 

Start by going to https://reeborg.ca/index_en.html where you learn to tell a robot how to get through mazes, jump over hurdles and more - I will highlight the first hurdle solution here to demonstrate - there are no python files in this repository.

Use the "World Info" button to see what the objectives are and how difficult the solution is. "Reeborg's basic keyboard" contains all the allowable functions for you to include: note there is no 'turn around' so you have to figure that out by yourself.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

The levels become progressively more difficult: however you can see your solutions and use them to build longer functions as you go along.