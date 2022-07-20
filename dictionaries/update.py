d1 = {'a':1, 'b':2}

stuff = {'c': 3, 'd': 4, 'e': 5, 'a': 'Apple'}
print(d1)
print(stuff)

d1.update(stuff)
print(d1)

d1 = {'a':1, 'b':2}
d2 = {'c': 3, 'a': 'ambulance'}

d3 = d1 | d2
print(d3)