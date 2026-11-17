"""
Use this list:
call_scores = [85, 92, 76, 95, 88, 65]



Combine enumerate(), if, and else to produce:
Call 1: 85 - PASS
Call 2: 92 - PASS
Call 3: 76 - FAIL
Call 4: 95 - PASS
Call 5: 88 - PASS
Call 6: 65 - FAIL
"""

call_scores = [85, 92, 76, 95, 88, 65]
threshold = 80

passed = 0
failed = 0

for index, score in enumerate(call_scores):
    if score >= threshold:
        print(f"Call {index+1}: PASS")
        passed += 1
    else:
        print(f"Call {index+1}: FAIL")
        failed += 1

print(f"Passed Calls: {passed}")
print(f"Failed Calls: {failed}")