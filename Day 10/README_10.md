# Day 10: Functions with Outputs

Normal functions:
```
def my_function():
    # do something
```
Functions with Inputs:
```
def my_function(something):
    # do this with something

my_function(123)
```
## Functions with Outputs:
```
def my_function():
    return 3 * 2
my_function()
```
terminal: 6

Example:
```
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name("ADELAINE", "SUHENDRO"))
```
_call the function in the print statement_

### Multiple Return Values
return tells the computer that it's the end of the function
```
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("What is your first name?"), input("What is your last name?")))
```
_if user did not input anything, terminal will display "Result:". Therefore, we need the if statement_

## EX 1: Days in Month
In starting code, is the Leap Year challenge code. 
1. Convert this function is_leap() so that it'll return True or False
2. Create function days_in_month() that takes a year and a month as inputs
```
days_in_month(year=2022, month=2)
```
3. Calculate the number of days in the month and return it as output

the list *month-days* are the months for a non-leap year. Leap year has 29 days in February

**HINTS: month_days is a List, starting at position 0. So, number of days in Jan is month_days[0]**