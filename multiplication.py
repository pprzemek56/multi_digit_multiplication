import sys


def main():
    a = input("a = ")
    b = input("b = ")

    print_multiplication(a, b)


def print_multiplication(a, b):
    try:
        main_product = int(a) * int(b)
    except ValueError:
        sys.exit("ERROR\n\na and b has to be int!")

    a_list = a[::-1]
    b_list = b[::-1]

    x = max(len(a_list), len(b_list))
    y = 2 + len(a_list)

    result = [[-1 for _ in range(x)] for _ in range(y)]
    print(result)

    for i in a_list:
        for j in b_list:
            ...





if __name__ == "__main__":
    main()
