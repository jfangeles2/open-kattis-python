def chanukahChallenge():
  inputLen = int(input())
  for i in range(inputLen):
    numOfNights = int(input().split(" ")[1])
    numOfCandlesLit = numOfNights/2*(2 + (numOfNights - 1)) + numOfNights
    print(str(i + 1) + " " + str(int(numOfCandlesLit)))

# ++++++++++++++++++++++++++++++
chanukahChallenge()