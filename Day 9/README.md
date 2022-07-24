# Day 8: Dictionaries and Nesting
{key : value}
EG:
```
programming_dictionary = {
"Function" : "a piece of code you can keep calling",
123 : "456"
}

print(programming_dictionary[123])
```
NOTE: "Function" is a string while 123 is an interger

### adding new items to dictionary / edit item in dictionary
```
programming_dictionary["Bug"] = "error"
```
### create empty dictionary
```
empty = {}
```
### wipe/erase existing dictionary
```
programming_dictionary = {}
```
### loop through a dictionary
NOTE: even if 'key' was not used or replaced with any other variable, the key will still be printed out
```
for key in programming:
    print(key)  #prints key
    print(programming_dictionary[key])    #prints value
```
## Nesting lists and dictionaries
{key: [list],
key2: {dict},}

### Nesting a List in a Dictionary
```
travel_log = {
"France" : ["Paris", "Lille", "Dijon"],
"Germany" : ["Berlin", "Stuttgart"]
}
```

### Nesting a Dictiionary in a Dictionary
```
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12}
}
```

### Nesting Dictionary in a List
[{
    key : [List],   
    key2 : {Dict},
},
{
    Key : value,
    Key2 : value,
}]

```
travel_log = [
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    {
       "country" : "Germany",
       "cities_visited" : ["Berlin", "Munich"],
       "total_visits" : 3
    },
]
```
## Grading Program
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades.
- a new dictionary called student_grades that should contain student names for keys and their grades for values

Hint: Remember that looping through a Dictionary will only give you the keys and not the values. At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

## Ex2: Dictionary in List
Write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
```
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
```
DO NOT modify the travel_log directly. You need to create a function that modifies it.

HINT: Look at the function call above to see what the name of the function should be.
The inputs for the function are positional arguments. The order is very important.
Feel free to choose your own parameter names.