print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# concatenate the string and then convert to lower case
combined_names = name1 + name2
lower_names = combined_names.lower()

# here the .count examines for how many times
# the letters "true love" appear
# NOTE a string value is returned which will be converted
# to integer when doing the final calculation
# first look for count of "true" and assign the count
# to a variable that the next programmer can find easy
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

# now add up the digits and save in new variable
first_digit = t + r + u + e

# repeat the process above for the word "love"
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# to determine the final score convert the numbers stored
# in a string to integer
# pylint identified score as a constant variable, ignore warning for now
score = int(str(first_digit) + str(second_digit))

# use if / elif / else logic to give user quirky message
# refactoring advised for line 42 to simplify chain comparison
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")