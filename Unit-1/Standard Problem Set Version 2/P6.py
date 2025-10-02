def squared(numbers):
    squaredlist = [x**2 for x in numbers]
    print(squaredlist)


if __name__ == '__main__':
    numbers = [1, 2, 3]
    squared(numbers)