#1. Structure: ()
tu = (10,20,30)
tu = (10,) # coma should be there other wise it will take it as a itn value
print(type(tu))

#2. Type of data: Heterogeneous
tu = (10,3.14,'abc')

#3. Sequence: ordered

#4 . Changable: Imutable
# tu[0]=30 it will raise the error because tuple does not support item assigment

#5. Duplication: Allowed.
tu = (10,20,30,40,50,50,60)
print(tu)