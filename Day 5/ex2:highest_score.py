#Calculate highest score using for loop, do not use max function

student_score = input("Score?").split( )
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
#--------------------------------------------
highest = 0
for score in student_score:
    if score > highest:
        highest = score
print(f"The highest score in class is: {highest}")