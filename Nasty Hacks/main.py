'''
3
0 100 70
100 130 30
-100 -70 40
'''
n = int(input())

for i in range(n):
  r,e,c = map(int,input().split(' '))
  if r > e - c:
    print('do not advertise')
  elif r == e - c:
    print('does not matter')
  else:
    print('advertise')