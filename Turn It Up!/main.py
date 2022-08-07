"""
5
Skru op!
Skru op!
Skru op!
Skru op!
Skru ned!
"""

numOfInputs = int(input())

vol = 7
for i in range(numOfInputs):
	command = input()
	if command == "Skru op!" and vol != 10:
		vol += 1
	if command == "Skru ned!" and vol != 0:
		vol -= 1

print(vol)
