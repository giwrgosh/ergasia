
number= input ("Πληκτρολογήστε τον ακέραιο θετικό αριθμό που θέλετε να μετατρέψετε (από 1-1000000):")
str(number)
if str(number) <str(0):
	import sys
	sys.exit("Ο αριθμός που δώσατε δεν είναι θετικός ακέραιος ")
	
	
def reversed_string(number):
    return number[::-1]

mystring1 = "0"
mystring2 = "0"
mystring3 = "0"
mystring4 = "0"
mystring5 = "0"
mystring6 = "0"
mystring7 = "0"
	
if len(number) == 1 :
	k = (reversed_string(number)[0])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
if len(number) == 2 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])

	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
if len(number) == 3 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])
	m = (reversed_string(number)[2])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
	
	if m == str(1):
		mystring3 = "C";
	if m == str(2):	
		mystring3 = "CC";
	if m == str(3):	
		mystring3 = "CCC";
	if m == str(4):	
		mystring3 = "CD";	
	if m == str(5):	
		mystring3 = "D";	
	if m == str(6):	
		mystring3 = "DC";	
	if m == str(7):	
		mystring3 = "DCC";	
	if m == str(8):	
		mystring3 = "DCCC";	
	if m == str(9):	
		mystring3 = "CM";
if len(number) == 4 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])
	m = (reversed_string(number)[2])
	n = (reversed_string(number)[3])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
	
	if m == str(1):
		mystring3 = "C";
	if m == str(2):	
		mystring3 = "CC";
	if m == str(3):	
		mystring3 = "CCC";
	if m == str(4):	
		mystring3 = "CD";	
	if m == str(5):	
		mystring3 = "D";	
	if m == str(6):	
		mystring3 = "DC";	
	if m == str(7):	
		mystring3 = "DCC";	
	if m == str(8):	
		mystring3 = "DCCC";	
	if m == str(9):	
		mystring3 = "CM";	
	
	if n == str(1):
		mystring4 = "M";
	if n == str(2):	
		mystring4 = "MM";
	if n == str(3):	
		mystring4 = "MMM";
	if n == str(4):	
		mystring4 = "MMMM";	
	if n == str(5):	
		mystring4 = "VVVVV";	
	if n == str(6):	
		mystring4 = "VVVVVM";	
	if n == str(7):	
		mystring4 = "VVVVVMM";	
	if n == str(8):	
		mystring4 = "VVVVVMMM";	
	if n == str(9):	
		mystring4 = "MXXXXX";	
	
	if o == str(1):
		mystring5 = "(X)";
	if o == str(2):	
		mystring5 = "(XX)";
	if o == str(3):	
		mystring5 = "(XXX)";
	if o == str(4):	
		mystring5 = "(XL)";	
	if o == str(5):	
		mystring5 = "(L)";	
	if o == str(6):	
		mystring5 = "(LX)";	
	if o == str(7):	
		mystring5 = "(LXX)";	
	if o == str(8):	
		mystring5 = "(LXXX)";	
	if o == str(9):	
		mystring5 = "(XC)";
if len(number) == 5 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])
	m = (reversed_string(number)[2])
	n = (reversed_string(number)[3])
	o = (reversed_string(number)[4])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
	
	if m == str(1):
		mystring3 = "C";
	if m == str(2):	
		mystring3 = "CC";
	if m == str(3):	
		mystring3 = "CCC";
	if m == str(4):	
		mystring3 = "CD";	
	if m == str(5):	
		mystring3 = "D";	
	if m == str(6):	
		mystring3 = "DC";	
	if m == str(7):	
		mystring3 = "DCC";	
	if m == str(8):	
		mystring3 = "DCCC";	
	if m == str(9):	
		mystring3 = "CM";	
	
	if n == str(1):
		mystring4 = "M";
	if n == str(2):	
		mystring4 = "MM";
	if n == str(3):	
		mystring4 = "MMM";
	if n == str(4):	
		mystring4 = "MMMM";	
	if n == str(5):	
		mystring4 = "VVVVV";	
	if n == str(6):	
		mystring4 = "VVVVVM";	
	if n == str(7):	
		mystring4 = "VVVVVMM";	
	if n == str(8):	
		mystring4 = "VVVVVMMM";	
	if n == str(9):	
		mystring4 = "MXXXXX";	
	
	if o == str(1):
		mystring5 = "(X)";
	if o == str(2):	
		mystring5 = "(XX)";
	if o == str(3):	
		mystring5 = "(XXX)";
	if o == str(4):	
		mystring5 = "(XL)";	
	if o == str(5):	
		mystring5 = "(L)";	
	if o == str(6):	
		mystring5 = "(LX)";	
	if o == str(7):	
		mystring5 = "(LXX)";	
	if o == str(8):	
		mystring5 = "(LXXX)";	
	if o == str(9):	
		mystring5 = "(XC)";
if len(number) == 6 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])
	m = (reversed_string(number)[2])
	n = (reversed_string(number)[3])
	o = (reversed_string(number)[4])
	p = (reversed_string(number)[5])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
	
	if m == str(1):
		mystring3 = "C";
	if m == str(2):	
		mystring3 = "CC";
	if m == str(3):	
		mystring3 = "CCC";
	if m == str(4):	
		mystring3 = "CD";	
	if m == str(5):	
		mystring3 = "D";	
	if m == str(6):	
		mystring3 = "DC";	
	if m == str(7):	
		mystring3 = "DCC";	
	if m == str(8):	
		mystring3 = "DCCC";	
	if m == str(9):	
		mystring3 = "CM";	
	
	if n == str(1):
		mystring4 = "M";
	if n == str(2):	
		mystring4 = "MM";
	if n == str(3):	
		mystring4 = "MMM";
	if n == str(4):	
		mystring4 = "MMMM";	
	if n == str(5):	
		mystring4 = "VVVVV";	
	if n == str(6):	
		mystring4 = "VVVVVM";	
	if n == str(7):	
		mystring4 = "VVVVVMM";	
	if n == str(8):	
		mystring4 = "VVVVVMMM";	
	if n == str(9):	
		mystring4 = "MXXXXX";	
	
	if o == str(1):
		mystring5 = "(X)";
	if o == str(2):	
		mystring5 = "(XX)";
	if o == str(3):	
		mystring5 = "(XXX)";
	if o == str(4):	
		mystring5 = "(XL)";	
	if o == str(5):	
		mystring5 = "(L)";	
	if o == str(6):	
		mystring5 = "(LX)";	
	if o == str(7):	
		mystring5 = "(LXX)";	
	if o == str(8):	
		mystring5 = "(LXXX)";	
	if o == str(9):	
		mystring5 = "(XC)";
	
	if p == str(1):
		mystring6 = "(C)";
	if p == str(2):	
		mystring6 = "(CC)";
	if p == str(3):	
		mystring6 = "(CCC)";
	if p == str(4):	
		mystring6 = "(CD)";	
	if p == str(5):	
		mystring6 = "(D)";	
	if p == str(6):	
		mystring6 = "(DC)";	
	if p == str(7):	
		mystring6 = "(DCC)";	
	if p == str(8):	
		mystring6 = "(DCCC)";	
	if p == str(9):	
		mystring6 = "(CM)";
if len(number) == 7 :
	k = (reversed_string(number)[0])	
	l = (reversed_string(number)[1])
	m = (reversed_string(number)[2])
	n = (reversed_string(number)[3])
	o = (reversed_string(number)[4])
	p = (reversed_string(number)[5])
	q = (reversed_string(number)[6])
	if k == str(1):
		mystring1 = "I";
	if k == str(2):	
		mystring1 = "II";
	if k == str(3):	
		mystring1 = "III";
	if k == str(4):	
		mystring1 = "IV";	
	if k == str(5):	
		mystring1 = "V";	
	if k == str(6):	
		mystring1 = "VI";	
	if k == str(7):	
		mystring1 = "VII";	
	if k == str(8):	
		mystring1 = "VIII";	
	if k == str(9):	
		mystring1 = "IX";	
	
	if l == str(1):
		mystring2 = "X";
	if l == str(2):	
		mystring2 = "XX";
	if l == str(3):	
		mystring2 = "XXX";
	if l == str(4):	
		mystring2 = "XL";	
	if l == str(5):	
		mystring2 = "L";	
	if l == str(6):	
		mystring2 = "LX";	
	if l == str(7):	
		mystring2 = "LXX";	
	if l == str(8):	
		mystring2 = "LXXX";	
	if l == str(9):	
		mystring2 = "XC";	
	
	if m == str(1):
		mystring3 = "C";
	if m == str(2):	
		mystring3 = "CC";
	if m == str(3):	
		mystring3 = "CCC";
	if m == str(4):	
		mystring3 = "CD";	
	if m == str(5):	
		mystring3 = "D";	
	if m == str(6):	
		mystring3 = "DC";	
	if m == str(7):	
		mystring3 = "DCC";	
	if m == str(8):	
		mystring3 = "DCCC";	
	if m == str(9):	
		mystring3 = "CM";	
	
	if n == str(1):
		mystring4 = "M";
	if n == str(2):	
		mystring4 = "MM";
	if n == str(3):	
		mystring4 = "MMM";
	if n == str(4):	
		mystring4 = "MMMM";	
	if n == str(5):	
		mystring4 = "VVVVV";	
	if n == str(6):	
		mystring4 = "VVVVVM";	
	if n == str(7):	
		mystring4 = "VVVVVMM";	
	if n == str(8):	
		mystring4 = "VVVVVMMM";	
	if n == str(9):	
		mystring4 = "MXXXXX";	
	
	if o == str(1):
		mystring5 = "(X)";
	if o == str(2):	
		mystring5 = "(XX)";
	if o == str(3):	
		mystring5 = "(XXX)";
	if o == str(4):	
		mystring5 = "(XL)";	
	if o == str(5):	
		mystring5 = "(L)";	
	if o == str(6):	
		mystring5 = "(LX)";	
	if o == str(7):	
		mystring5 = "(LXX)";	
	if o == str(8):	
		mystring5 = "(LXXX)";	
	if o == str(9):	
		mystring5 = "(XC)";
	
	if p == str(1):
		mystring6 = "(C)";
	if p == str(2):	
		mystring6 = "(CC)";
	if p == str(3):	
		mystring6 = "(CCC)";
	if p == str(4):	
		mystring6 = "(CD)";	
	if p == str(5):	
		mystring6 = "(D)";	
	if p == str(6):	
		mystring6 = "(DC)";	
	if p == str(7):	
		mystring6 = "(DCC)";	
	if p == str(8):	
		mystring6 = "(DCCC)";	
	if p == str(9):	
		mystring6 = "(CM)";
	
	if q == str(1):
		mystring7 = "(M)";

	
	
print ("Οποιοδήποτε από τα γράμματα βρίσκεται σε παρεν8έσεις() τότε είναι το αντίστοιχο γράμμα με μία γραμμή από πάνω.")

if mystring7!= str(0) :
	print (mystring7,end="")
if mystring6!= str(0) :
	print (mystring6,end="")
if mystring5!= str(0) :
	print (mystring5,end="")
if mystring4!= str(0) :
	print (mystring4,end="")
if mystring3!= str(0) :
	print (mystring3,end="")
if mystring2!= str(0) :
	print (mystring2,end="")
if mystring1!= str(0) :
	print (mystring1,end="")