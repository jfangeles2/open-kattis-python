# Splits the string in half. Only works with even length strings
def divide(string):
	partLen = int(len(string)/2)
	return [string[:partLen], string[partLen:]]

# Gets the corresponding val of the letter
def getVal(letter):
	# Get the desired value by subtracting 65
	# from the ascii value of the letter
	return ord(letter) - 65

# Gets the letter of the val
def getLetter(integer):
	# Get the desired value by adding 65
	# to make it equal to ascii vals
	return chr(integer + 65)

# Gets the rotation value of the string
def getRotationVal(strSeq):
	val = 0
	for i in range(len(strSeq)):
		val = val + getVal(strSeq[i])
	return val

# Adjusts the letter by the num of positions, and returns new letter
def adjustLetter(numOfPositions, letter):
	# because there are only 26 letters
	# so 27 adjustments == 1 adjustment
	actualAdjustments = numOfPositions % 26
	return getLetter((actualAdjustments + getVal(letter)) % 26)


# Rotates the string using a rotation value
def rotateStr(inputStr, rotVal):
	convertedList = []
	for i in range(len(inputStr)):
		convertedList.append(adjustLetter(rotVal, inputStr[i]))
	# ''.join(listInstance) does not work when there are
	# elements that are not str
	return ''.join(convertedList)

# Rotates the string using another string
def rotateStringWithString(s1, s2):
	word = []
	for i in range(len(s1)):
		word.append(adjustLetter(getVal(s2[i]) ,s1[i]))
	return ''.join(word)


########
# MAIN
########

inputStr = input()
# inputStr = "EWPGAJRB"
# inputStr = "UEQBJPJCBUDGBNKCAHXCVERXUCVK"

# Divide
fPart, sPart = divide(inputStr)

# Rotate
rVal1 = getRotationVal(fPart)
rVal2 = getRotationVal(sPart)

nString1 = rotateStr(fPart, rVal1)
nString2 = rotateStr(sPart, rVal2)

print(rotateStringWithString(nString1, nString2))
