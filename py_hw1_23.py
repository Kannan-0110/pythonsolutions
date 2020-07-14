class student:
    std={}
    def read(self,name,section,sem,usn,gender,subjectmarks):
        self.std={'name':name,'section':section,'usn':usn,'sem':sem,'gender':gender,'subjectmarks':subjectmarks}
    def display_details(self):
        percent=0
        print("Name: ",self.std['name'])
        print("Section: ",self.std['section'])
        for key,value in self.std['subjectmarks'].items():
            percent+=value
            print(key,":",value)
        percent=(percent/600)*100
        print("percent: ",round(percent,2),"%")
        
n=int(input("enter the number of students: "))
stdict=dict()
for i in range(n):
    name=input("\nenter the name: ")
    section=input("enter the section: ")
    usn=input("enter the USN: ")
    sem=int(input("enter the Sem: "))
    gender=input("enter the Gender: ")
    
    sub1=int(input("subject 1 mark: "))
    sub2=int(input("subject 2 mark: "))
    sub3=int(input("subject 3 mark: "))
    sub4=int(input("subject 4 mark: "))
    sub5=int(input("subject 5 mark: "))
    sub6=int(input("subject 6 mark: "))
    subjectmark={'mark 1':sub1,'mark 2':sub2,'mark 3':sub3,'mark 4':sub4,'mark 5':sub5,'mark 6':sub6}

    s=student()
    s.read(name,section,usn,sem,gender,subjectmark)
    stdict[usn]=s
usn=input("\nenter the usn to search: ")
s=stdict[usn]
s.display_details()
        
