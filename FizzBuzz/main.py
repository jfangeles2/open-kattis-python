a,b,n = map(int, input().split(" "))

i = 1
while i != n + 1:
  if i % a == 0:
    if i % b == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif i % b == 0:
    print("Buzz")
  else:
    print(i)
  i = i + 1
