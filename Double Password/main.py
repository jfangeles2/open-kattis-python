# # test 1
# pass1 = "1111"
# pass2 = "1234"
# # test 2
# pass1 = "2718"
# pass2 = "2718"


# MAIN
pass1 = input()
pass2 = input()

differentChars = 0
for i in range(4):
	if pass1[i] != pass2[i]:
		differentChars += 1
print(pow(2, differentChars))