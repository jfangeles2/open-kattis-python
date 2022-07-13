txt = input()
y = txt.find("a")
if y == -1:
  print(txt)
else:
  print(txt[y:])