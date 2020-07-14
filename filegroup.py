import os
import re
from shutil import copy
path="C:\\Users\\kanna\\Desktop\\New folder"
arr = os.listdir(path)
dates={}

for i in arr:
    s=re.search("[0-9]{8}",i)
    r=re.search("[\w]*-[0-9]{8}",i)
    if s:
        if r:
            if s.group() in dates: 
                dates[s.group()]=dates[s.group()]+[r.group(),]
            else:
                dates[s.group()]=[r.group(),]
print(dates)
for i in dates.keys():
    os.mkdir(path+"\\"+i)
for i,j in dates.items():
    for k in j:
        copy(path+"\\"+k+".txt", path+"\\"+i)