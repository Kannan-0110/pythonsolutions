import re
f=open('maildata.txt','r')
mail='[\w\.-]+@[\w\.-]+'
phnbr='(0/91)?[7-9][0-9]{9}'
for line in f:
    em=re.search(mail,line)
    pn=re.search(phnbr,line)
    if em:
        print(em.group())
    if pn:
        print(pn.group())
