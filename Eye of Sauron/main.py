txt = input().split("()")
# print(txt)

# This try-except block is there to catch the test case when there is no () in the string
try:
  if txt[0] == txt[1]:
    print("correct")
  else:
    print("fix")
except:
  print("fix")