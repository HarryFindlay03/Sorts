import random

n = int(input("Enter Length of List: "))
numbers = [random.randint(0, 1000000) for x in range(0, n)]

# Clears the file of any numbers that are already in it
f = open('numbers.txt', 'r+')
f.truncate(0)
f.close()

with open('numbers.txt', 'w') as file:
	for item in numbers:
		file.write("%s, " % item)
file.close()
