#using a module - this one is to generate random numbers
import random

# a seed number means that we are giving the random function
# a point to start at manually
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# variable randomSide refers to a coin having two sides
randomSide = random.randint(0, 1)
if randomSide == 1:
    print("Heads")
else:
    print("Tails")