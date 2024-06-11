# Question 1
### Algorithmic Questions (Pseudocode):

**Question:** Write a function that takes an array of integers and returns the sum of the two largest numbers in the array.
```
# Write pseudocode solution here
```

function two_largest_sum(arr):

    # edge case empty list
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    #sort array
    arr.sort()

    # return sum of last two elements
    return arr[len(arr) - 1] + arr[len(arr) - 2]