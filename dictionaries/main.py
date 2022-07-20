d1 = {1: 'One'}

d2 = d1
d2[2] = 'two'
d3 = d1.copy()
d1 == d3
print(d3)

d1.clear()
print(d1)
