def count_stuff(*args):
    print(f"you passed me {len(args)} arguments")

count_stuff(4,5,6, True, False, -1)

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum(4,6,7,8))

def silly(first, second, *others):
    print(f"first is: {first}")
    print(f"second is: {second}")
    print(f"others is: {others}")

silly(1,2,3,4,5,6,True, False, ['hello', 'goodbye'])


def silly_goose(num, *args):
    return args

print(silly_goose(1,2,3,4,5))


def login(first, *args):
    print("does nothing")

print(login('charlie'))


def count(x, y, *args):
    return len(args)

print(count(56, 99, True, 'chicken', 1))
