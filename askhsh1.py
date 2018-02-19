import random
a = [int(x) for x in input("Δώστε τους 5 αριθμού σας από το 1 έως και το 80, χωρίς επανάληψη αριθμών, χωρισμένους με κόμματα(,) : ").split(',')]
number1 = a[0]
number2 = a[1]
number3 = a[2]
number4 = a[3]
number5 = a[4]
if number1 > 80:
	import sys
	sys.exit("Ο πρώτος αριθμός που δώσατε είναι μεγαλύτερος του 80 ")
if number1 < 1:
	import sys
	sys.exit("Ο πρώτος αριθμός που δώσατε είναι μικρότερος του 1 ")
if number2 > 80:
	import sys
	sys.exit("Ο δέυτερος αριθμός που δώσατε είναι μεγαλύτερος του 80 ")
if number2 < 1:
	import sys
	sys.exit("Ο δεύτερος αριθμός που δώσατε είναι μικρότερος του 1 ")
if number3 > 80:
	import sys
	sys.exit("Ο τρίτος αριθμός που δώσατε είναι μεγαλύτερος του 80 ")
if number3 < 1:
	import sys
	sys.exit("Ο τρίτος αριθμός που δώσατε είναι μικρότερος του 1 ")
if number4 > 80:
	import sys
	sys.exit("Ο τέταρτοσ αριθμός που δώσατε είναι μεγαλύτερος του 80 ")
if number4 < 1:
	import sys
	sys.exit("Ο τέταρτος αριθμός που δώσατε είναι μικρότερος του 1 ")
if number5 > 80:
	import sys
	sys.exit("Ο πέμπτος αριθμός που δώσατε είναι μεγαλύτερος του 80 ")
if number5 < 1:
	import sys
	sys.exit("Ο πέμπτος αριθμός που δώσατε είναι μικρότερος του 1 ")
if number1 == number2 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number1 == number3 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number1 == number4 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number1 == number5 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number2 == number3 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number2 == number4 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number2 == number5 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number3 == number4 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number3 == number5 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
if number4 == number5 :
	import sys
	sys.exit("Δύο αριθμοί ταυτίζονται")	
sum = 0




for k in range(0, 999):
	numbers = []
	paikths = []
	paikths.append(number1)
	paikths.append(number2)
	paikths.append(number3)
	paikths.append(number4)
	paikths.append(number5)
	for i in range(81):
		numbers.append(i)
	del numbers[0]
	players = []
	for i in range(100):
		players.append([])
		random.shuffle(numbers)
		players[i].append(numbers[0])
		players[i].append(numbers[1])
		players[i].append(numbers[2])
		players[i].append(numbers[3])
		players[i].append(numbers[4])	
	
	
	find = False
	for i in range(80):
		 
		random.shuffle(numbers)
		a = numbers[0]
		del numbers[0]
		sum= sum + 1	
		if a in paikths:
			paikths.remove(a)
		for n in range(100):
			if a in players[n]:
				players[n].remove(a)
		if not paikths:	
			
			find = True
			break
		for n in range(100):
			if not players[n]:
			
				find = True
				break
		if   find:
			break
			
			
apotelesma = float(sum/1000)	
print ("Ο μέσος όρος των αριθμών που πρέπει να να αναγγελθούν ώστε να έχουμε Bingo είναι: ",apotelesma)	