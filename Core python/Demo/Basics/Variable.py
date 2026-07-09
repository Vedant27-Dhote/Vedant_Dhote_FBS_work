###Rules to define Varibale names
# 1. can contain alphabets, digits, underscore
# 2. can't contain symbol except underscore
# 3. can't contain space
# 4. can't start with number
# 5. Can't use keywords as a varibale name
# 6. 

#will run
num = 10
num_1 = 10
print(num)

#will not run
# num@20 = 1  # error due to symbol
# total marks = 100 # error due to space used
# 10num = 40 #error due to start with number
#def = 10 # error due to keyword used

# To print adress of variable
print(id(num))
print(id(num_1))