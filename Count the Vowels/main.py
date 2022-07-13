inputStr = input().lower()

vowels = {"a", "e", "i", "o", "u"}

count = 0
for i in range(len(inputStr)):
  if inputStr[i] in vowels:
    count += 1

print(count)