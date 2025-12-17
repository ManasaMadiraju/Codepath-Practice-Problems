'''Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.'''


def sum_of_digits(num):
    new_list = list(map(int, str(num)))
    sum = 0 
    for i in new_list:
        sum += i
    return sum


if __name__ == '__main__':
    num = 423
    print(sum_of_digits(num))

    num = 4
    print(sum_of_digits(num))