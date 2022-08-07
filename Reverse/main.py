def reverse(inputList):
	for i in range(len(inputList)):
		print(inputList.pop(-1))


###
numOfInputs = int(input())
inputList = []
for i in range(numOfInputs):
	inputList.append(int(input()))
reverse(inputList)