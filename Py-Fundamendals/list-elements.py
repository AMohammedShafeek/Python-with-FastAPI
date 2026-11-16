"""
Call Score Analyzer
Beginner

You're given these scores:
call_scores = [85, 92, 76, 95, 88]



Write Python code to calculate and print:
Total Calls: 5
Highest Score: 95
Lowest Score: 76
Average Score: 87.2
"""

callScores = [85, 92, 76, 95, 88]

print(f"Total Calls: {len(callScores)}")
print(f"High Score: {max(callScores)}")
print(f"Low Score: {min(callScores)}")
print(f"Average Score: {sum(callScores)/len(callScores)}")