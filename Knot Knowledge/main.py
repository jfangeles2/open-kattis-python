"""
4
1 2 4 3
4 2 3
= 1

4
10 101 999 1
1 999 101
= 10
"""

toBeLearned = int(input())

target = set(map(int, input().split(" ")))
learned = set(map(int, input().split(" ")))

print(target.difference(learned).pop())