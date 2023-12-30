def FindGCD(x,y):
	while(y>0):
		r=x%y
		x=y
		y=r
	return x
	
a=int(input())
b=int(input())
print("The GCD of",a," and ",b,"is : ",end=" ")
print(FindGCD(a,b))
