# Question 5
# Python-Specific Questions:
# Question: Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the input list.

# Code solution here


def filter_even_numbers(numbers):
    
    # Returns a list of even numbers from the input list.
    # :param numbers: List of integers
    # :return: List of even integers
    

    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(input_list)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
