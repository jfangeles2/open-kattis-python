def isPositive(number):
  return number > 0

a = int(input())
b = int(input())

if isPositive(a):
  if isPositive(b):
    print(1)
  else:
    print(4)
else:
  if isPositive(b):
    print(2)
  else:
    print(3)
