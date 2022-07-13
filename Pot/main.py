numOfInput = int(input())

ans = 0
for i in range(numOfInput):
  a = int(input())
  ans = ans + (int(a/10)**(a%10))

print(ans)