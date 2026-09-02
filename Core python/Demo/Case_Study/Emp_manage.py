from Hr import Hr
from Dev import Dev

class EmployeeManagement:
    def __init__(self):
        self.edetils = {}

    def addEmp(self):
        empid = int(input("Enter the Id of Emp: "))
        if empid in self.edetils:
            print("Emp Already Exists")
            return 
        else:
            name = input("Enter the Name of Emp: ")
            sal = float(input("Enter the Sal of Emp: "))
            print("1. Hr")
            print("2. Developer")
            choice = int(input("Enter Your Choice = "))
            if choice == 1:
                com = float(input("Enter the Com of Hr = "))
                emp = Hr(empid, name, sal, com)
            elif choice == 2:
                bonus = float(input("Enter the Bonus of Developer = "))
                emp = Dev(empid, name, sal, bonus)
            else:
                print("Invalid choice ....")
                return
            self.edetils[empid] = emp
            print("Emp Added successfully.... ")

    def displayEmp(self):
        if len(self.edetils) == 0:
            print("Employee does not Exist...")
        else:
            for emp_id, empobj in self.edetils.items():
                print(empobj)

    def searchEmp(self):
        if len(self.edetils) == 0:
            print("Employee does not Exist...")
        else:
            eid = int(input("Enter the Id of Employee: "))
            if eid in self.edetils:
                print("EmpDetail =", self.edetils[eid])
            else:
                print(f"Employee with {eid} is not present ")

    def updateEmp(self):
        if len(self.edetils) == 0:
            print("Employee does not Exist...")
        else:
            eid = int(input("Enter the Id of Employee: "))
            if eid in self.edetils:
                empobj = self.edetils[eid]
                print("EmpDetail =", empobj)
                name = input("Enter the Name of Emp: ")
                sal = float(input("Enter the Sal of Emp: "))
                empobj.setName(name)
                empobj.setSal(sal)
                print("Emp Updated successfully.... ")
            else:
                print(f"Employee with {eid} is not present ")

    def delEmp(self):
        if len(self.edetils) == 0:
            print("Employee does not Exist...")
        else:
            eid = int(input("Enter the Id of Employee: "))
            if eid in self.edetils:
                del self.edetils[eid]
                print(f"Employee with {eid} is Deleted ")
            else:
                print(f"Employee with {eid} is not present ")
