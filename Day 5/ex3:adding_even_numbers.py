#Adding even numbers from 1 to 100 using the for loop and range() function
total = 0
for number in range(0, 101, 2):
    total += number
print(total)

#Alternative
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)