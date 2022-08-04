# *args Gathers all remaining arguments into a tuple.
# You can name the parameter "args" what you want.
# args is common but NOT required.

def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total//len(args)

print(average(2,3,4,5,6,7,8))

