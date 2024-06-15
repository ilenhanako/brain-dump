# LEETCODE: Data Structures and Algorithms

## Content
1. Leetcode questions done are arranged by month
2. Notes
3. Test: Interview questions tested

## Tips:
1. enumerate(): Need both item and values in a list
- LC: TwoSum

```python
fruits = ['apple','banana','pear']
#index: 0,1,2
#values: apple, banana, pear

#wrong way
index = 0
for fruit in fruits:
    print("Index: " + index + ", Value: " + fruit) #some action
    index += 1
```

```python
#do this
for index, fruit in enumerate(fruits)
```

2. Slicing 
- LC: 344ReverseString
**[start:stop:step]**

```python
mylist = [10, 20, 30, 40, 50, 60, 70, 80]
result = mylist[1:6] #getting second to sixth element
result1 = mylist[2:] #getting third to last element
```
**Step: [::2]** means stepping through objects by 2

> Reverse Element in list or string: 
>
> In more complex problems: s = s[::-1] won't work
> WORK: s[:] = s[::-2]
> WORK!!!! : reversed(mylist)
>
> Since it creates a new list, it may not be what we want
