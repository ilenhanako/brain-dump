# using the random module we incorporate a seed number input
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method - note that it is defined as comma followed by space
names_input = input("Give me everybody's names, seperated by a comma and a space. ")
names = names_input.split(", ")

# Get the total number of items in list using len()
num_items = len(names)

# Generate random numbers between 0 and the last index
# the choice() function not used as we need to work with how
# the indices are addressed
random_choice = random.randint(0, num_items - 1)

# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")