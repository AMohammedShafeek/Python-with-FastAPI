"""
Create a Python program that stores the following information:
- Product name: Conversa-IQ
- Total calls: 1500
- Evaluated calls: 1200
- Average score: 87.5
- Evaluation active: True
Then print the product name and calculate the number of pending calls.
"""

data = {
    "productName": "ConversaIQ",
    "totalCalls": 1500,
    "EvaluatedCalls": 1200,
    "AvgScore": 87.5,
    "EvalActive": True,
}
pendingCalls = data["totalCalls"]-data["EvaluatedCalls"]
completedPerc = (data["EvaluatedCalls"]/data["totalCalls"])*100

print(f"Product Name: {data["productName"]}")
print(f"Pending Calls: {pendingCalls}")
print(f"Percentage of Completed Calls:{completedPerc}%")