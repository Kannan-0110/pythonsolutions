import re
f=open('maildata3.txt','r')
p="Date: (Mon|Tue|Wed|Thu|Fri|Sat), \d{1,2} (Jan|Feb|Mar|Apr|May|Jun|July|Aug|Sept|Oct|Nov|Dec) \d{4}"
for line in f:
    msg=re.match(p,line)
    if msg:
        print(msg.group())
    
