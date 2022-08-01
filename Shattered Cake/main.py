"""
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
"""

width = int(input())
pieces = int(input())

area = 0
for i in range(pieces):
	l, w = map(int, input().split(" "))
	area += (l * w)
print(int(area/width))
