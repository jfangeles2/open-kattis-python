# 4
# 21
# 34
# 18
# 9

# 79
numberOfJavelins = int(input())
ans = 0
for i in range(numberOfJavelins):
  ans = ans + int(input())
print(ans - numberOfJavelins + 1)