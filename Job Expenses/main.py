"""
10
-100 40000 -6500 -230 -18 34500 -450 13000 -100 5000
= 7398
"""

n = int(input())
expenses = []
data = input().split(" ")[:n]

for item in data:
	a = int(item)
	if a < 0:
		expenses.append(a)

print(sum(expenses) * -1)
