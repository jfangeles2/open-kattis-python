inputs = int(input())

ans = 0
for i in range(inputs):
    lineArgs = input().split(' ')
    ans = ans + float(lineArgs[0]) * float(lineArgs[1])
print(ans)
    