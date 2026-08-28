fs = frozenset({10,20,30,40})
fs2 = frozenset({30,40,50,60})

'''Methods'''

new = fs.copy()
print(new)
print(fs.difference(fs2))
print(fs.intersection(fs2))
print(fs.isdisjoint(fs2))
print(fs.issubset(fs2))
print(fs.issuperset(fs2))
print(fs.symmetric_difference(fs2))
print(fs.union(fs2))
