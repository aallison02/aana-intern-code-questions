# Question 2
### Algorithmic Questions (Pseudocode):
**Question:** Implement a function that checks if a given string is a palindrome (reads the same forwards and backwards). The function should ignore case and non-alphanumeric characters.
```
# Write pseudocode solution here
```

function is_palindrome(string):
    filtered_string = ''

    for char in string:
        if char is alphanumeric
            append to filtered_string
    
    left_ptr = 0
    right_ptr = filtered_string.length() - 1

    while left_ptr < right_ptr:
        if filtered_string[left_ptr] != filtered_string[right_ptr]:
            return False
        else:
            left_ptr += 1
            right_ptr -= 1
    
    return true

