x = [1, 2, 2, 2, 554, 45, 45, 25, 25, 55, 2, 78, 99, 99]
x_copy = x.copy()
for number in x:
	if x.count(number) > 1:
		x.remove(number)
print(x)

#or populate a new list with singles
uniques = []
for nr in x:
	if nr not in uniques: # checking to see if the nt is not in the uniques list
		uniques.append(nr) # populate uniques with nr
print(uniques)
print(x_copy) #printing original list copy