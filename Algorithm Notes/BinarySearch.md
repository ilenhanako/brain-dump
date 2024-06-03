# Binary Search 
## O(logn) , n = size(array)

- If the target exists, returns its leftmost index. Else, returns the index of where it should be

`binarySearch(nums: List[int], target: int) → int`
 - input: nums and target
 - input type: nums is a list of int, target is an int
 - output type: int

```
def binarySearch(nums: List[int], target: int) → int:
	l, r = 0, len(nums)
	while l < r:
		m = (l + r) // 2
		if nums[m] < target:
			l = m + 1
		else:
			r = m
	return l
```

### Explanation of Code:
1. Initatialization
   - `l` and `r` = left and right boundaries of search space.
   - `l` set to 0
   - `r` set to length of array`nums`
2. Binary Search Loop:
   - `while` loop continues as long as `l` < `r`, ensuring there is a valid search space.
   - `m`, middle index is the midpoint of the current search space

### Summary
- Code searches target in sorted array. 
- Narrows down search space by comparing middle element and adjusting the boundaries accordingly. 
- Returned index = correct position for inserting the target to maintain a sorted order