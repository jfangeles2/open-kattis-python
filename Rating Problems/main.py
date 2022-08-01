"""
5 2
1
2
"""

judges, judgesRated = map(int, input().split(" "))
judgesUnrated = judges - judgesRated
ratingList = []

for i in range(judgesRated):
	ratingList.append(int(input()))

minRatingNumerator = sum(ratingList) + (-3 * judgesUnrated)
maxRatingNumerator = sum(ratingList) + (3 * judgesUnrated)

print(minRatingNumerator/judges, end=" ")
print(maxRatingNumerator/judges)
