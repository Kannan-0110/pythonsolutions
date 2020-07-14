n=int(input("enter the value of n "))
lst1=[]
mx=0
res=[]
for i in range(n):
      m=int(input("enter the size of tuple "))
      if(m>mx):
          mx=m
      print("enter tuple elements ")
      t=()
      for i in range(m):
          k=int(input())
          t=t[0:]+(k,)
      lst1.append(t)

for i in range(mx):
    t=()
    k=1
    for j in lst1:
        if(len(j)>i):
            t=t[0:]+(j[i]**k,)
            k+=1
    res.append(t)   
print(res)
    
      
      
    
      
