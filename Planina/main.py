'''
Solved using excel and visualization.
The number of boxes is predictable.
Multiply the number of boxes of the last
iteration by 4 to get the number of boxes
of the next iteration. The number of points
per row is the number of boxes per row + 1.
'''
iteration = int(input())
print(((2**iteration) + 1)**2)
