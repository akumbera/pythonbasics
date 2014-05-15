#This function calculates posiives integers up to 1990
def primerec(x, y= -1):
	if y== -1:
		y=x
		primerec(x,y)
	else:
		if x<=1:
			print 'Error: enter an integer greater than 1.'
		elif x==2:
			if y==x:
				print str(y) + ' is prime'
			elif y%x==0:
				print str(y) + ' is not prime.'
			else:
				print str(y) + ' is prime.'
		else:
			if x>2:
				x=x-1
				if y%x==0:
					print str(y) + ' is not prime.'
				else:
					primerec(x,y)

#This function works for positive, odd integers up to 2,147,399,999
#Even integers can be arbitrarily large, as far as I can tell.
def primeloop(y):
	if y<=1:
		print 'Error: enter an integer greater than 1.'
	elif y==2:
		print str(y) + ' is prime.'
	elif y==3:
		print str(y) + ' is prime.'
	elif y%2==0:
		print str(y) + ' is not prime.'
	else:
		for x in xrange(3,y,2):
			if y%x==0:
				print str(y) + ' is not prime.'
				break
			elif x==(y-2):
				print str(y) + ' is prime.'


"""
def primearray(y):
	siv=[2]
	for x in xrange(0,len(siv)):
		if y%siv[x]==0:
			print str(y) + ' is not prime.'
		elif x=len(siv):
			siv.append(y)
			print siv
"""