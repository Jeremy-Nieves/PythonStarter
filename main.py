def main():
    total = 0

    while not total:
        print("Give me two numbers")
        val1 = input("First Number: ")
        val2 = input("Second Number: ")

        if not isAlpha(val1, val2):

            total = sum(int(val1), int(val2))

    print(total)


def sum(num1, num2):
    return num1 + num2


def isAlpha(val1, val2):
    return val1.isalpha() or val2.isalpha()


if __name__ == "__main__":
    main()