class college:
    def __init__(self,name,place,pincode):
        self.college_name=name
        self.college_place=place
        self.college_pincode=pincode
    def getCDetails(self):
        print("College: ",self.college_name,"\nPlace: ",self.college_place,"\nPincode: ",self.college_pincode)

class student(college):
    def __init__(self,name,usn,branch,college_name,college_place,college_pincode):
        self.name=name
        self.usn=usn
        self.branch=branch
        college.__init__(self,college_name,college_place,college_pincode)

    def getStdDetails(self):
        print("name: ",self.name,"\nUsn: ",self.usn,"\nBanch: ",self.branch)

s=student("Kannan","4jk17cs025","cse","AJIET","mangaluru",575013)
s.getStdDetails()
s.getCDetails()

        
        
        
