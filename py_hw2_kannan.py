import re
f=open('maildata.txt','r')
r="(Delivered-To: |To: |From: [A-Za-z\s]* <)([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})>?"
for line in f:
    msg=re.search(r,line)
    if msg:
        k=re.search("([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})",msg.group())
        print(k.group())
    
