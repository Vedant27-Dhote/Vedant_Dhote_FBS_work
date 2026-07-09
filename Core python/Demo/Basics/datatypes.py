### Numeric
#1. int
var = 10
print(type(var))

#2. float
var = 10.6
print(type(var))

#3. Complex
var = 10+3j   # Real + imaginary
print(type(var))


### Text
#1. string
var = 'Vedant Dhote'
print(type(var))
var = "Vedant Dhote"
print(type(var))
var = ''' Vedant  
        Dhote'''  # Multiline string
print(type(var))


### Sequential
#1. list
var = [10,20,30,40]
print(type(var))

#2. tuple
var = (10,20,30,40)
var = 10,20,30,40   # Another way to write tuple
print(type(var))

#3. Range
var = range(1,10)
print(type(var))

### Set type
#1.set 
var = {10,20,30,40}
print(type(var))

#2. forzenset
var = frozenset({10,20,30,40})
print(type(var))


### Mapping
var = {'id':101,'name':'Vedant','Salary':50000}
print(type(var))

### other
#1. Bool
var = True
print(type(var))

#2. none
var = None
print(type(var))