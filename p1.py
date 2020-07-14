def findn(s):
    for i in range(s)[::-1]:
        if(i**2<s):
            break
    k=i
    while(k>0):
        l=s-k**2
        for j in range(k+1):
            if(j**2==l):
                return [k,j]
        k-=1
        
     
while(True):
    n=int(input("enter the value of N : "))
    if(n==-1):
        break
    res = findn(n)
    print(res)
