import math

def theAmazingHumanCannonball():
  testCases = int(input())
  for i in range(testCases):
    velocity, angle, distance, heightBottom, heightTop = map(float, input().split(" "))
    
    timeAtXPos = distance / (velocity * math.cos(math.radians(angle)))
    yPos = (velocity * timeAtXPos * math.sin(math.radians(angle))) - (1/2*9.81*(timeAtXPos**2))
    
    if yPos > heightBottom + 1 and yPos < heightTop - 1:
      print("Safe")
    else:
      print("Not Safe")


theAmazingHumanCannonball()
