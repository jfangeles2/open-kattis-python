"""
30 30 27 27
35 30 25 29
30 35 30 35
"""

wc, hc, ws, hs = map(int, input().split(" "))

if wc - ws >= 2 and hc - hs >= 2:
	print(1)
else:
	print(0)