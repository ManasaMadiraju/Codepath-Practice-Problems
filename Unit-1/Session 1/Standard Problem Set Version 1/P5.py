'''Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().'''

def sum_honey(hunny_jars):
    sum = 0
    for i in hunny_jars:
        sum += i
    print(sum)

if __name__ == '__main__':
    hunny_jars = [2, 3, 4, 5]
    sum_honey(hunny_jars)

    hunny_jars = []
    sum_honey(hunny_jars)

