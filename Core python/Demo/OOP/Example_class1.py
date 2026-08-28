class FBSStudent:
    count = 0
    def __init__(self,frn,name,batch):
        self.frn = frn
        self.name=name
        self.batch = batch
        FBSStudent.count+=1

    def getFrn(self):
        return self.frn
    def setFrn(self,Newfrn):
        self.frn = Newfrn

    def getName(self):
        return self.name
    def setName(self,Newname):
        self.name = Newname

    def getbatch(self):
        return self.batch
    def setbatch(self,Newbatch):
        self.batch = Newbatch


    def display(self):
        print(f"Frn={self.frn} name={self.name} batch={self.batch}")


class Placed_student(FBSStudent):
    def __init__(self, frn, name, batch,cName):
        super().__init__(frn, name, batch)
        self.cName=cName

    def getcName(self):
        return self.cName
    def setcName(self,newcName):
        self.cname=newcName

    def display(self):
        super().display()
        print(f"Cname={self.cName}")

s1=FBSStudent(1,"Rahul","june26")
s2=FBSStudent(17,"Ab-devilliers","June26")
s3=Placed_student(18,"Virat","June26","one8")
s3.display()



