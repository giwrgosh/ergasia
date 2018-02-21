import urllib.request, urllib.error, urllib.parse
import json
import datetime
cur_date=datetime.datetime.now()
a = [int(x) for x in input("Εισάγετε τους 10 αριθμούς σας χωρισμένους με κόμμα(,): ").split(',')]
number1 = a[0]
number2 = a[1]
number3 = a[2]
number4 = a[3]
number5 = a[4]
number6 = a[5]
number7 = a[6]
number8 = a[7]
number9 = a[8]
number10 = a[9]
y = 0
b = ""
def compare_lists(l1,l2,y,b):

	s=0
	for i in l1:
		if i in l2:
			s+=1
			if y < s + 1:		
				y = s
				b = (date_str)			
	print (b)
	return (y,s, b)

mynums = []	
mynums.append(number1)
mynums.append(number2)
mynums.append(number3)
mynums.append(number4)
mynums.append(number5)
mynums.append(number6)
mynums.append(number7)
mynums.append(number8)
mynums.append(number9)
mynums.append(number10)

for i in range(31):
	cur_date= cur_date - datetime.timedelta(days=1)
	date_str= cur_date.strftime("%d-%m-%Y")
	url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	data = response.read()
	data=json.loads(data)
	klhrwseis= data['draws']['draw']
	r=[]
	for k in klhrwseis:
		tmp=k["results"]
		r.append(compare_lists(mynums,tmp,y,b))
	
print ("Η ημέρα στην οποία έχεται τις περισσότερες πιθανότητες νίκης στο Κίνο είναι η τελευταία ημερομηνία")