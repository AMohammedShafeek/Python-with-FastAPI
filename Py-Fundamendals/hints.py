"""
Take this function:
def calculate_average(scores):    return sum(scores) / len(scores)



Your task: Add type hints so that:
- scores accepts a list of integers: list[int]
- The function returns a floating-point number: float
Then call the function using:
call_scores = [85, 92, 76, 95, 88]



Expected output:
Average Score: 87.2


Don't change the calculation logic. Just add the correct type hints and print the result using an f-string.
"""

def calculate_average(scores: list[int]) -> float:    return sum(scores) / len(scores)

call_scores = [85, 92, 76, 95, 88]

print(f"{calculate_average(call_scores):.1f}")

"""
Quick practice
Now I want you to try a slightly different function.

Create:
def calculate_total(scores: list[int]) -> int:    # Your code here



Using:
call_scores = [85, 92, 76, 95, 88]



Expected output:
Total Score: 436


Your task: Complete the function using sum() and call it correctly without a loop.
"""

scores = [85, 92, 76, 95, 88]

def calculate_total(scores: list[int]) -> int:
    return sum(scores)

print(f"Total: {calculate_total(scores)}")

"""
Create a function called get_call_score().

Starting code:

call_data = {    
    "call_id": 101,    
    "score": 87,    
    "duration": 240
}

def get_call_score(call: dict[str, int]) -> int:    
    
    # Your logic here



Your task: Return the value of "score" from the dictionary and print it.

Expected output:
Call Score: 87


Use an f-string and call the function with the entire call_data dictionary.
"""

call_data = {    
    "call_id": 101,    
    "score": 87,    
    "duration": 240
}

def get_call_score(call: dict[str, int]) -> int:
    return call["score"]

print(f"Call Score: {get_call_score(call_data)}")

"""
Create a function:
def get_call_score(call: dict[str, int | None]) -> int | None:    # Your code

Use this data:

call_data = {
    "call_id": 101,
    "score": None,
    "duration": 240
}

Your task: Call the function and print one of these results:

If the score is None:
Call 101: Evaluation Pending

If the score is available, for example 87:
Call 101: Score - 87

Hints: Use .get("score"), if score is None, and else.

Try writing it yourself. Test your program twice — first with score = None, then with score = 87.
"""

call_data = {
    "call_id": 101,
    "score": None,
    "duration": 240
}

def get_score(call: dict[str, int | None]) -> int | None:
    return call["score"]

score = get_score(call_data)

if score is None:
    print("Call Processing...")

else:
    print(f"Score: {score}")