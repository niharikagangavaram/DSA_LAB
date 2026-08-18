def power (P, n) :
    if n==0:
        return 1
    else:
        return P * power (P, n- 1)
P= float (input ("Enter principal growth factor (P): "))
n = int (input ("Enter number of years (n) ="))
result=power(P,n)
print ("Power =", result)
