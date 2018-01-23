#!/usr/bin/python


#欧几里德算法求出两个数的最大公约数
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a % b)

def simpleRationNumber(tuple_number):
	if tuple_number[0] == 0:
		return str(0)
	result_str = ''
	commonNumber = gcd(tuple_number[0], tuple_number[1])
	mol = tuple_number[0] // commonNumber
	den = tuple_number[1] // commonNumber
	abs_mol = abs(mol)
	abs_den = abs(den)
	if abs_mol >= abs_den:
		if abs_mol % abs_den == 0:
			result_str = str(abs_mol // abs_den)
		else:
			result_str = str(abs_mol // abs_den)+' '+str(abs_mol % abs_den)+'/'+str(abs_den)
	else:
	   result_str = str(abs_mol)+'/'+str(abs_den)
	if mol * den > 0:
		return result_str
	else:
		return '(-'+result_str+')'	
		



def operationRationalNumber(number1,number2,symbol):
	if symbol == '+':
		mol = number1[0] * number2[1] + number1[1] * number2[0]
		den = number1[1] * number2[1]
		return simpleRationNumber((mol, den))
	if symbol == '-':
		mol = number1[0] * number2[1] - number1[1] * number2[0]
		den = number1[1] * number2[1]
		return simpleRationNumber((mol, den))
	if symbol == '*':
		mol = number1[0] * number2[0]
		den = number1[1] * number2[1]
		return simpleRationNumber((mol, den))
	if symbol == '/':
		if number2[0] == 0:
			return 'Inf'
		mol = number1[0] * number2[1]
		den = number1[1] * number2[0]
		return simpleRationNumber((mol, den))
	
row_line = input()

n1,n2 = row_line.split()
tuple_n1 = tuple([int(x) for x in n1.split('/')])
tuple_n2 = tuple([int(x) for x in n2.split('/')])


print(simpleRationNumber(tuple_n1),'+',simpleRationNumber(tuple_n2),'=',operationRationalNumber(tuple_n1,tuple_n2,'+'))
print(simpleRationNumber(tuple_n1),'-',simpleRationNumber(tuple_n2),'=',operationRationalNumber(tuple_n1,tuple_n2,'-'))
print(simpleRationNumber(tuple_n1),'*',simpleRationNumber(tuple_n2),'=',operationRationalNumber(tuple_n1,tuple_n2,'*'))
print(simpleRationNumber(tuple_n1),'/',simpleRationNumber(tuple_n2),'=',operationRationalNumber(tuple_n1,tuple_n2,'/'))





