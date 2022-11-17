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

    result = [[-1 for _ in range(final_x)] for _ in range(final_y)]

    x = final_x - 1
    y = final_y - 1

    counter = 0

    while y >= 0:
        while x >= 0:
            if counter == 0 and x < len(a_list):
                if len(a_list) < len(b_list):
                    result[y][x + len_dif] = a_list[x]
                else:
                    result[y][x] = a_list[x]
            elif counter == 1 and x < len(b_list):
                if len(b_list) < len(a_list):
                    result[y][x + len_dif] = b_list[x]
                else:
                    result[y][x] = b_list[x]
            x -= 1
        if counter == 2:
            a_list.reverse()
            b_list.reverse()
            y = 0
            for i in range(len(a_list)):
                for j in range(len(b_list)):
                    mul = int(a_list[i]) * int(b_list[j])
                    if result[final_y - 3 - i][final_x - 1 - j] != -1:
                        mul += result[final_y - 3 - i][final_x - 1 - j]
                    if mul > 9 and result[final_y - 2][final_x - 2 - j] != -1:
                        result[final_y - 3 - i][final_x - 2 - j] = int(mul / 10)
        counter += 1
        x = final_x - 1
        y -= 1

    print(result)




if __name__ == "__main__":
    main()
