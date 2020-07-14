import re
strin=input("enter the string")
p='([0|91|+91]?\d{10,12})'
mat=re.findall(p,strin)
print(mat)
