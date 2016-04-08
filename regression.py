import numpy
from numpy import matrix

def regression(y,X):
	#generalized linear regression formula
	B_vector=(X.H*X)**(-1)*X.H*y
	
	#if values are really small, lets just make them 0 for simplicity
	for values in range(len(B_vector)):
		if B_vector[values]<.000000000001 and B_vector[values] > -.00000000001:
			B_vector[values]=0
	
	#returns the coefficients
	return B_vector

#sum of squares error
def sse(y, X, B_vector):
	this_thing=(y-X*B_vector)
	sserror=0
	for values in this_thing:
		sserror=sserror+values**2

		
	return sserror
	
#mean square error
def mse(y,X,B_vector):
	ssError=sse(y,X,B_vector)
	ase=ssError/len(X)
	return ase


y=matrix("[2;4;6;8;10;12;14;16;18;20]")
X=matrix("[1 2 1;1 5000000 2;1 6 3;1 8 50;1 10 5;1 12 6;1 14 7;1 16 50;1 18 9;1 20 10]")
print y
print X

print regression(y,X)
print 'SSE={0}'.format(sse(y,X,regression(y,X)))
print 'MSE={0}'.format(mse(y,X,regression(y,X)))