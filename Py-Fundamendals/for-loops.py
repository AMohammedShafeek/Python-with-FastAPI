"""
Using this list:
call_scores = [85, 92, 76, 95, 88]



Write a for loop that prints each score like this:
Call Score: 85
Call Score: 92
Call Score: 76
Call Score: 95
Call Score: 88


Don't use five separate print statements. Use one for loop and an f-string.
"""

call_scores = [85, 92, 76, 95, 88]

for index, score in enumerate(call_scores):
    print(f"Call Score {index+1}: {score}")