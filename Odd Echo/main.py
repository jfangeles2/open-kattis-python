def oddEcho():
  entries = int(input())
  wordsToEcho = []
  for i in range(entries):
    if i % 2 == 0:
      wordsToEcho.append(input())
    else:
      input()
  for word in wordsToEcho:
    print(word)




oddEcho()

