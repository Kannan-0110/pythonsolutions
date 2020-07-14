n=int(input("enter the number of students"))
lst=[]
for i in range(n):
    name=input()
    usn=int(input())
    lst.append((name,usn))
rng=int(input("enter the range"))
for i,j in lst:
    if j in range(rng):
        print(tuple(i,j))
             
             
