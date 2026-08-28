def emp(Id,Name,Sal=150,dept="It"):
    print("Id:",Id)
    print("NAme:",Name)
    print("Salary:",Sal)
    print("Department:",dept)

emp(99,"Vedant",75000,"DA")  # We assing all value so default values get overwrite by new values

emp(89,"Jos",75000) # The dept parameter will take default value so that It