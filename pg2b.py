import re
f=open("maildata.txt","r")
r='(From:|To:)( *\S* *)*\S+@\S*.\S*'
fr=""
to=""
r2='\S+@\S*.\S'
for line in f:
	match=re.search(r,line)
	print(match)
	if match:
		id=match.group()
		if "From" in id:
			fr=re.findall(r2,id)[0]
		elif "To" in id:
			to=re.findall(r2,id)[0]
print("From : ",fr)
print("To : ",to)