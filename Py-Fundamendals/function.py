"""
Write a Python program that:
1. Creates a function named evaluate_call(score).
2. Returns "PASS" when the score is 80 or above, otherwise "FAIL".
3. Uses a for loop to evaluate all six scores.
4. Prints each call number, score, and result.
Use:
call_scores = [85, 92, 76, 95, 88, 65]



Expected output:
Call 1: 85 - PASS
Call 2: 92 - PASS
Call 3: 76 - FAIL
Call 4: 95 - PASS
Call 5: 88 - PASS
Call 6: 65 - FAIL
"""

call_scores = [85, 92, 76, 95, 88, 65]

def evaluate_call(score: int, threshold: int =80):
    if score >= threshold:
        return "PASS"
    else:
        return "FAIL"

threshold = 90
for index, score in enumerate(call_scores):
    print(f"Call {index+1}: Score - {score} - Status: {evaluate_call(score, threshold)}")