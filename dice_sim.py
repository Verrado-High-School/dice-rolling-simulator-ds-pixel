import random

num_rolled = int(input("How many times will the dice be rolled?"))


ones = 0
twos = 0
threes = 0
fours = 0 
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0

i = 0

while i < num_rolled:
	i += 1
	D4 = random.randrange(1, 5, 1)
	D6 = random.randrange(1, 7, 1)
	D8 = random.randrange(1, 9, 1)
	D10 = random.randrange(1, 11, 1)
	D12 = random.randrange(1, 13, 1)
	D20 = random.randrange(1, 21, 1)

	print("Roll " + str(i) + "-------------" + "\n" + "Dice 1 (1,4): "+ str(D4) + "\n" + "Dice 2 (1,6): " + str(D6))

	if D4 == 1:
		ones += 1
	elif D4 == 2:
		twos += 1
	elif D4 == 3:
		threes += 1
	elif D4 == 4:
		fours += 1

	if D6 == 1:
		ones += 1
	elif D6 == 2:
		twos += 1
	elif D6 == 3:
		threes += 1
	elif D6 == 4:
		fours += 1
	elif D6 == 5:
		fives += 1
	else:
		sixes += 1
	
	print("1s - " + str(ones))
	print("2s - " + str(twos))
	print("3s - " + str(threes))
	print("4s - " + str(fours))
	print("5s - " + str(fives))
	print("6s - " + str(sixes))


	print("Percentages:")
	print("1s - " + str(ones/(2*i)*100) + "%")
	print("2s - " + str(twos/(2*i)*100) + "%")
	print("3s - " + str(threes/(2*i)*100) + "%")
	print("4s - " + str(fours/(2*i)*100) + "%")
	print("5s - " + str(fives/(2*i)*100) + "%")
	print("6s - " + str(sixes/(2*i)*100) + "%")


