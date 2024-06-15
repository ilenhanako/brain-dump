# Array Cheatsheet
## Time Complexity
1. Add or Remove at END of array:
**O(1)** (Amortized)
- Sometimes have to increase amount of memory available

2. Add or Remove NOT at END of array:
**O(n)** 
- since there is a need to adjust all other positions

3. Access Element at an Index:
**O(1)** 
- CONSTANT since it is just simple indexing

4. Searching for an Element in Array:
**O(n)** 
- loop through the array to find it

5. Searching SORTED array for element:
**O(log(n))** 
- use BINARY SEARCH

6. Copying Array:
**O(n)**

7. Sliding Window:
**O(n)**

8. Need all pairs of array elements:
**O(n^2)**