def fibo(n):
    if (n==0) or (n==1) :
        return n
    return fibo(n-1)+fibo(n-2)

a=int(input())
print(fibo(a))
