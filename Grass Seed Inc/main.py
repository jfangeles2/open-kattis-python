cost = float(input())

n = int(input())

c = 0
for i in range(n):
  a,b = map(float, input().split(' '))
  c = c + a*b
print(c*cost)