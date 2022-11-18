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

    a_list = [_ for _ in a]
    b_list = [_ for _ in b]

    len_dif = abs(len(a_list) - len(b_list))
    final_x = max(len(a_list), len(b_list))
    final_y = 2 + len(a_list)

    multiplication_array = [[-1 for _ in range(final_x)] for _ in range(final_y)]
    add_array = [[-1 for _ in range(len(a_list) + len(b_list))] for _ in range(len(a_list))]

    x = final_x - 1
    y = final_y - 1

    counter = 0
    while y >= 0:
        while x >= 0:
            if counter == 0 and x < len(a_list):
                if len(a_list) < len(b_list):
                    multiplication_array[y][x + len_dif] = a_list[x]
                else:
                    multiplication_array[y][x] = a_list[x]
            elif counter == 1 and x < len(b_list):
                if len(b_list) < len(a_list):
                    multiplication_array[y][x + len_dif] = b_list[x]
                else:
                    multiplication_array[y][x] = b_list[x]
            x -= 1
        if counter == 2:
            a_list.reverse()
            b_list.reverse()
            y = 0
            second_counter = 0
            for i in range(len(a_list)):
                for j in range(len(b_list)):
                    mul = int(a_list[i]) * int(b_list[j])
                    if multiplication_array[final_y - 3 - i][final_x - 1 - j] != -1:
                        mul += multiplication_array[final_y - 3 - i][final_x - 1 - j]
                    if mul > 9 and multiplication_array[final_y - 2][final_x - 2 - j] != -1:
                        multiplication_array[final_y - 3 - i][final_x - 2 - j] = int(mul / 10)
                result = int(b) * int(a_list[i])
                third_counter = len(add_array[0]) - 1 - second_counter
                while result > 0:
                    add_array[second_counter][third_counter] = result % 10
                    result = int(result / 10)
                    third_counter -= 1
                second_counter += 1
        counter += 1
        x = final_x - 1
        y -= 1

    for i in range(len(multiplication_array)):
        for j in range(len(multiplication_array[0])):
            if j == 0:
                if i == len(multiplication_array) - 1:
                    print("*", end=" " * len(add_array[0]))
                else:
                    print(" ", end=" " * len(add_array[0]))
            if multiplication_array[i][j] != -1:
                print(multiplication_array[i][j], end="")
            else:
                print(" ", end="")
        print()
    print("---" * len(multiplication_array[0]))

    for i in range(len(add_array)):
        for j in range(len(add_array[0])):
            if j == 0:
                if i == len(add_array) - 1:
                    print("+", end=" " * len(multiplication_array[0]))
                else:
                    print(" ", end=" " * len(multiplication_array[0]))
            if add_array[i][j] != -1:
                print(add_array[i][j], end="")
            else:
                print(" ", end="")
        print()
    print("---" * len(multiplication_array[0]))

    print(" " * (len(multiplication_array[0]) + 1), main_product)


if __name__ == "__main__":
    main()
