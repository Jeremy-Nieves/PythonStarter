# Created by Jeremy Nieves 7/6/22
def sum(num1, num2):
    if num1 or num2 is None:
        return None

    elif num1 != type(int) or num2 != type(int):
        print("Arguments not integers")
        return None

    return num1 + num2