def add_twice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    return lst

print(add_twice('hi'))
print(add_twice('boo'))

def add_thrice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice(7,[1,2,3]))
print(add_thrice(99))

def add_quad(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_quad(99))