"""
2 2 1 4
= 3.307189138830738

The maximum quadrilateral problem can be solved
using the Brahmagupta’s formula.
"""
import math

a,b,c,d = map(int, input().split(" "))

semiperimeter = (a + b + c + d)/2

print(math.sqrt((semiperimeter - a) * (semiperimeter - b) * (semiperimeter -c) * (semiperimeter - d)))
