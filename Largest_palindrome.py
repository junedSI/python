def is_palindrome(num):                 #function to check is palindrome.
    str_num = str(num)
    return str_num == str_num[::-1]


def main():                             #main def
    largest = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    print(largest)


if __name__ == '__main__':              #main
    main()
