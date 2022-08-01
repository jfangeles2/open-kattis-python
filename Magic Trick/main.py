"""
robust

icpc
"""

stringInput = input()
charList = []

for i in range(len(stringInput)):
	charList.append(stringInput[i])

for i in range(len(stringInput)):
	poppedChar = charList.pop(0)
	if poppedChar in charList:
		print(0)
		break

if len(charList) == 0:
	print(1)
