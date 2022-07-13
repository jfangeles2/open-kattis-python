'''
10
3
4
6
2
'''

mbPerMonth = int(input())
numOfMonths = int(input())

mbAvailable = mbPerMonth
for i in range(numOfMonths):
  mbAvailable = mbAvailable + mbPerMonth - int(input())
print(mbAvailable)