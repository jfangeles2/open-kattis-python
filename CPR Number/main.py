def cprNumber(inputStr):
	valSeq = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
	idStr = inputStr.replace("-", "")

	total = 0
	for i in range(10):
		total += (int(idStr[i]) * valSeq[i])

	if total % 11 == 0:
		print(1)
	else:
		print(0)


################
# cprNumber("070761-4285")
# cprNumber("051002-4321")
# cprNumber("310111-0469")
cprNumber(input())