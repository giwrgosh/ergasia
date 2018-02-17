import random
number1= input ("Δώστε τον πρώτο αριθμό σας (από το 1 έως το 80): ")
number2= input ("Δώστε τον δεύτερο αριθμό σας (από το 1 έως το 80): ")
number3= input ("Δώστε τον τρίτο αριθμό σας (από το 1 έως το 80): ")
number4= input ("Δώστε τον τέταρτο αριθμό σας (από το 1 έως το 80): ")
number5= input ("Δώστε τον πρώτο αριθμό σας (από το 1 έως το 80): ")
paikths = []
paikths.extend((number1, number2, number3, number4, number5))
sum = 0
numbers = []
for i in range(81):
	numbers.append(i)
del numbers[0]
random.shuffle(numbers)
players = []
for i in range(100):
	players.append([])

	random.shuffle(numbers)
	players[i].append(numbers[0])
	players[i].append(numbers[1])
	players[i].append(numbers[2])
	players[i].append(numbers[3])
	players[i].append(numbers[4])
	

for i in range(80):
	random.shuffle(numbers)
	a = numbers[0]
	b = []
	del numbers[0]
	sum= sum + 1
	if a in paikths:
		paikths.remove(a)
	for n in range(100):
		if a in players[n]:
			players[n].remove(a)
	if not paikths:
			print ("bob")
			break		
	for n in range(100):
		if  players[n]:
			print ("reerr")
			break
	
		else:
			continue
		break
print(*players, sep="\n")	
print (sum)
print (paikths)

		