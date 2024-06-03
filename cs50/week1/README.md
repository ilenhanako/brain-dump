# Lecture 1: C. IDEs, Compilers, Interfaces. Syntax and Rules in code.

## IDEs, Compilers, Interfaces.
IDE = Integrated Development Environments, allow us to write/run our code. 
- Eg: VSCode

__Source Code (Code that we read/write) --(converted to)--> Machine Code (0s and 1s)__
- Compilers are used to convert

__Terminals:__ provides CLI(command-line interface), allows us to compile, connects us to operating system(macOS)

## Code:
- Functions (arguments, return values)
- Conditionals
- Boolean Expressions (True/False)
- Loops
- Variables
__Correctness, Design(Write well), Style__

## C: Remember your (;)
hello.c
```
#include <stdio.h>
int main(void)
{
    printf("hello, world\n");
}
```
Next, convert to machine code(binary)
_Terminal:_
> make hello 
make = a program that knows how to use the compiler in the system, thus "compiles" it or makes the file
> ./hello 
. means go to current folder, / means run the program in the folder)
> rm hello 
(rm means remove)
__Command lines__
- cd (change directory/folder or goes to the default folder)
 - cd .. (change to parent directory)
 - cd../..(change to grandparent directory)

- cp (copy)
- ls (list)
- mkdir (make directory/folder)
- code name.c (makes and opens file)
- mv (move/rename)
- rm (remove)
 - rmdir(remove directory)
### Functions and Arguments
```
printf("Hello World!");
```
- f in printf refers to a "formatted" string
__Return Values, Variables__
- gives you back an output that you can reuse
Function and variables:
```
string answer = get_string("What's your name?");
```
- (=) is an assignment operator means assigning a value
- Need to assign type at the start (string, int, boolean)
- (\n) is an escape sequence, creates a new line
- __Library:__ common set of code, _stdio.h_ is the library for standard input and output functions

```
#include <cs50.h>
#include <stdio.h>
int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer):
}
```
- (%s) placeholder for printf to _format_ our string, we pass in the variable as another argument with __answer__, separating it from the first argument with (__,__)

_Terminal:_
> hello.c:5:5 
error found on line 5, character 5

### Types
__get_string__ replace string with the respective types
- String
- Int (Numbers)
- Boolean (True/False)
- Char (single character)
- Double (more numbers after decimal pt)
- Float (Decimal)
- Long (bigger integer)

### Format Code
- %c (char)
- %f (float/double)
- %i (int)
- %li (long)
- %s (string)

### Operators
+-*/%
% is the modulus

### Variables/Synthetic Sugar
```
int counter = 0;
```
All the same:
```
counter = counter + 1;
counter += 1;
counter++;
```

### Comments in C
add //