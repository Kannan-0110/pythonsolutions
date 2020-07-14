import os
import re
from shutil import move
path="C:\\Users\\kanna\\Pictures\\New folder"
arr = os.listdir(path)
dates={}

for i in arr:
    r=re.search("(IMG(_)?[2014|2015|2016|2017|2018|2019|2020])[\w]*",i)
    if r:
        res=r.group()
        if 'IMG_' in res:
            yer=res.replace('IMG_','')[:4]
        else:
            yer=res.replace('IMG','')[:4]
        if yer in dates: 
            dates[yer]=dates[yer]+[res,]
        else:
            dates[yer]=[res,]
for i in dates.keys():
    os.mkdir(path+"\\"+i)
for i,j in dates.items():
    for k in j:
        move(path+"\\"+k+".jpg", path+"\\"+i)
