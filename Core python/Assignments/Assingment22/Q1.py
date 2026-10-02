import pickle


class Emp:

    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic


def load_data():
    try:
        with open("emp.dat", "rb") as f:
            return pickle.load(f)
    except:
        return []


def save_data(employees):
    with open("emp.dat", "wb") as f:
        pickle.dump(employees, f)


def add_record():
    employees = load_data()

    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)
    employees.append(emp)

    save_data(employees)

    print("Record added successfully.")


def search_record():
    employees = load_data()

    eid = int(input("Enter Employee ID to search: "))

    for emp in employees:
        if emp.eid == eid:
            print("Employee ID:", emp.eid)
            print("Employee Name:", emp.ename)
            print("Basic Salary:", emp.basic)
            return

    print("Record not found.")


def delete_record():
    employees = load_data()

    eid = int(input("Enter Employee ID to delete: "))

    new_list = []
    found = False

    for emp in employees:
        if emp.eid == eid:
            found = True
        else:
            new_list.append(emp)

    if found:
        save_data(new_list)
        print("Record deleted successfully.")
    else:
        print("Record not found.")


def edit_record():
    employees = load_data()

    eid = int(input("Enter Employee ID to edit: "))

    for emp in employees:
        if emp.eid == eid:

            emp.ename = input("Enter new name: ")
            emp.basic = float(input("Enter new basic salary: "))

            save_data(employees)

            print("Record updated successfully.")
            return

    print("Record not found.")


def display_records():
    employees = load_data()

    if len(employees) == 0:
        print("No records found.")
        return

    for emp in employees:
        print("-------------------------")
        print("Employee ID:", emp.eid)
        print("Employee Name:", emp.ename)
        print("Basic Salary:", emp.basic)

    print("-------------------------")


while True:

    print("\n===== EMPLOYEE MENU =====")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_record()

    elif choice == 2:
        search_record()

    elif choice == 3:
        delete_record()

    elif choice == 4:
        edit_record()

    elif choice == 5:
        display_records()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")