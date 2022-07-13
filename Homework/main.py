# Input: A string containing an integer, or a string with format "1-3"
# Output: The number of problems for in the input
def getProblemCount(inputStr):
  inputList = inputStr.split("-")
  # No - means 1 prob only
  if len(inputList) == 1:
    return 1
  # - means more than 1 prob
  else:
    return int(inputList[1]) - int(inputList[0]) + 1


# Main function
def homework():
  inputList = input().split(";")
  inputLen = len(inputList)
  numberOfProblems = 0
  for i in range(inputLen):
    numberOfProblems += getProblemCount(inputList[i])
  print(numberOfProblems)

#####################################
homework()