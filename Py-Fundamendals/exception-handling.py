"""
Write a function:
def divide_calls(total: int, count: int) -> float:    # Your code



Your function should divide total by count.

Test these two cases:
print(divide_calls(100, 5))print(divide_calls(100, 0))



Expected output:
20.0
Cannot divide by zero


Hint: Use try, except ZeroDivisionError, and return.
"""

def divide_calls(total: int, count: int) -> float :
    try:
        return total/count
    except ZeroDivisionError:
        return 0.0

print(divide_calls(100, 0))

"""
Handling Multiple Exceptions
Let's learn how to handle different errors in the same function.

Python allows multiple except blocks:
try:    # Code that might fail    ...except ZeroDivisionError:    # Handle division by zero    ...except TypeError:    # Handle invalid data types    ...



For example, dividing 100 / "five" raises a TypeError because Python cannot divide an integer by a string.
Your next challenge
Modify your existing divide_calls() function to handle both errors.
Input	Expected output
divide_calls(100, 5)	20.0
divide_calls(100, 0)	Cannot divide by zero
divide_calls(100, "five")	Invalid input type

Important: Because your function will now return either a number or an error message, change its return type to float | str.
"""

def divide_calls_func(total: int, count: int) -> float | str :
    try:
        return total/count
    except ZeroDivisionError:
        return "Cant Divide by Zero"
    except TypeError:
        return "Invalidd Data Type"

print(f"{divide_calls_func(100, 5)}")
print(f"{divide_calls_func(100, 0)}")
print(f"{divide_calls_func(100, "5")}")