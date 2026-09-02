from Emp_manage import EmployeeManagement

class Login:    
    def login():
        Id = "Admin"
        password = 1234
        entered_id = input("Enter your username: ")
        entered_password = int(input("Enter your password: "))

        if Id == entered_id and password == entered_password:
            print("Login successful")
            
            emp_manager = EmployeeManagement()
            
            while True:
                print("\nEnter 1 for ADD Emp")
                print("Enter 2 for Display Emp")
                print("Enter 3 for Search Emp")
                print("Enter 4 for Update Emp")
                print("Enter 5 for Delete Emp")
                print("Enter 6 for Exit")
                ch = int(input("Enter the choice: "))
                
                if ch == 1:
                    emp_manager.addEmp()
                elif ch == 2:
                    emp_manager.displayEmp()
                elif ch == 3:
                    emp_manager.searchEmp()
                elif ch == 4:
                    emp_manager.updateEmp()
                elif ch == 5:
                    emp_manager.delEmp()
                elif ch == 6:
                    print("Exiting the program...")
                    break
        else:
            print("Invalid username or password")


Login.login()
