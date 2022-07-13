# [-1::-1] means start at the end of the str up to the start (denoted by the blank part. Decrement by 1 denoted by the last -1)
a,b = map(int, input()[-1::-1].split(" "))

if a > b:
  print(a)
else:
  print(b)