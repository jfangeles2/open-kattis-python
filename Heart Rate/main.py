# 2
# 6 5.0000
# 2 3.1222

n = int(input())

for i in range(n):
  a,b = map(float, input().split(' '))
  abpmOffset = 60/b
  bpm = 60*a/b
  print(str(bpm - abpmOffset) + ' ' + str(bpm) + ' ' + str(bpm + abpmOffset))