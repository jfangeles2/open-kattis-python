"""
EWPGAJRB
= ABCD
UEQBJPJCBUDGBNKCAHXCVERXUCVK
= ACMECNACONTEST
"""

# Get the desired value by subtracting 65
# from the ascii value of the letter
def getVal(letter):
	return ord(letter) - 65

# Get the desired value by adding 65
# to make it equal to ascii vals
def getLetter(integer):
	return chr(integer + 65)

def getRotationVal(strSeq):
	val = 0
	for i in range(len(strSeq)):
		val += getVal(strSeq[i])
	return val

def adjustLetter(numOfPositions, letter):
	# because there are only 26 letters
	# so 27 adjustments == 1 adjustment
	actualAdjustments = numOfPositions % 26
	return getLetter((actualAdjustments + getVal(letter)) % 26)

# ''.join(listInstance) does not work when there are
# elements that are not str
def rotateStr(inputStr, rotVal):
	convertedList = []
	for i in range(len(inputStr)):
		convertedList.append(adjustLetter(rotVal, inputStr[i]))
	return ''.join(convertedList)




inputStr = input()
# Divide
firstPart = inputStr[:(len(inputStr)/2)]
secondPart = inputStr[(len(inputStr)/2):]
print(firstPart)
print(secondPart)
# Rotate
rotValFirst = getRotationVal(firstPart)
rotValSecond = getRotationVal(secondPart)

rotated1 = rotateStr(firstPart, rotValFirst)
rotated2 = rotateStr(secondPart, rotValSecond)

msg = []
for i in range(len(rotated1)):
	msg.append(adjustLetter(getVal(rotated2[i]), rotated1[i]))
print(msg)