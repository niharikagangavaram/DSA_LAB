def fibanacci(a,b,n):
    if n==0:
        return
    print(a,end=" ")
    fibanacci(b,a+b,n-1)
n=int(input("enter the number of terms:"))
fibanacci(0,1,n)
