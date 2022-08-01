"""
10 3 4
2 1 5
5 2 3 7 8 10
3 2 7 10
1 8
"""

numOfCards, pred, steps = map(int, input().split(" "))

for i in range(steps):
	cardsChosen = list(map(int, input().split(" ")))
	# Remove the first element of the list to get the list of cards chosen
	cardsChosen.pop(0)
	if pred in cardsChosen:
		print("KEEP")
	else:
		print("REMOVE")
