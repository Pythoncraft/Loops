numbers=[250, 250, 7, 1, 75]
max_nr = numbers[0] # set max nr to first in the list
for number in numbers: #create loop through the list
	if number > max_nr: #condition to compare the loop number to max
		max_nr = number # if condition is true - set max number to that loop number
print(max_nr)