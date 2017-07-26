def karatsuba(x,y):
	if(len(str(x)) == 1 or len(str(y)) == 1):
		return x*y
	else:
		n=max(len(str(x)),len(str(y)))
		nHalf = n/2
		a = x/10**(nHalf)
		c = y/10**(nHalf)
		b = x%10**(nHalf)
		d = y%10**(nHalf)
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		adPlusbd = karatsuba(a+b,c+d)-ac-bd
		xy = ac*10**(nHalf*2)+adPlusbd*10**(n/2)+bd
		return xy
#Testing
#print karatsuba(99999,1000)
