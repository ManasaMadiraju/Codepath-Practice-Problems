'''Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.'''

def squared(numbers):
    squaredlist = [x**2 for x in numbers]
    print(squaredlist)


if __name__ == '__main__':
    numbers = [1, 2, 3]
    squared(numbers)