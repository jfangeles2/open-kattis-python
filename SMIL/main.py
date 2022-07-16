# Going through the whole will go through each character atmost once. I think this is better than going through the whole string 4 times by using str.find() and putting the smiles inside the function.
def SMIL():
  # smile_list = {":)", ";)", ":-)", ";-)"}
  strInput = input()
  i = 0
  smileIndices = []
  while i < len(strInput):
    # Checks for :) and :-)
    if strInput[i] == ":":
      try:
        # :) will append index to list and skip the ) part by appending 2 to i
        if strInput[i + 1] == ")":
          smileIndices.append(i)
          i += 2
          continue
        # :-) will append index to list and skip the -) part by appending 3 to i
        elif strInput[i + 1:i + 3] == "-)":
          smileIndices.append(i)
          i += 3
          continue
      # last char is :    
      except:
        pass

    # Checks for ;) and ;-)
    if strInput[i] == ";":
      try:
        # ;) will append index to list and skip the ) part by appending 2 to i  
        if strInput[i + 1] == ")":
          smileIndices.append(i)
          i += 2
          continue
        # ;-) will append index to list and skip the -) part by appending 3 to i
        elif strInput[i + 1:i + 3] == "-)":
          smileIndices.append(i)
          i += 3
          continue
      # Except for instances that the last char is ;
      except:
        pass
    
    i += 1

  for i in smileIndices:
    print(i, end = ' ')
  print()


# for i in range(4):
SMIL()
