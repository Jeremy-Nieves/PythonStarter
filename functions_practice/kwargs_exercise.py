# **kwargs = key word args

def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is {v} years old")

print_ages(max=67,sue=59,kim=14)

# or

def print_ages(**ages):
    for k,v in ages.items():
        print(f"{k} is {v} years old")

print_ages(max=67,sue=59,kim=14)

# order matters
# (parameters -> *args -> default parameters -> **kwargs)

def display_info(person,*args, status='single', **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

display_info('colt',1,2,3,4,status="married",age=87,mood="thrilled")





