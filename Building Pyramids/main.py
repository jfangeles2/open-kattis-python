# I never knew that one day I would choose recursion over loops
# 2022/07/16
def makeARow(numberOfBlocks, iteration):
  blocksLeft = numberOfBlocks - ((2 * iteration + 1)**2)
  # print("Blocks left is " + str(blocksLeft))
  if blocksLeft < 0:
    return 0
  elif blocksLeft == 0:
    return 1
  else:
    return 1 + makeARow(blocksLeft, iteration + 1)


def buildingPyramids():
  numberOfBlocks = int(input())
  print(makeARow(numberOfBlocks, 0))

buildingPyramids()