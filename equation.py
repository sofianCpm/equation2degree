import math
def solveGeneralEquation (a,b,c) :
	delta= b**2-4*a*c 
	if delta < 0:
		return ('equation has no solution', 'equation has no solution')
	if delta == 0:
		solution= -b/(2*a)
		return (solution,solution)
	else:
		solution1= (-b-(math.sqrt(delta)))/(2*a)
		solution2= (-b+(math.sqrt(delta)))/(2*a)
		return (solution1,solution2)
a=raw_input('enter a:')
a=int(a)

b=raw_input('enter b:')
b=int(b)

c=raw_input('enter c:')
c=int(c)


result=solveGeneralEquation(a,b,c)
print 'solution 1 is '
print result[0]

print 'solution2 is '
print result[1]
