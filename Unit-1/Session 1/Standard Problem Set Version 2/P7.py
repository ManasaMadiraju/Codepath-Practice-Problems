'''Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.'''

def nanana_batman(x):
    result = ""
    for i in range(x):
        result += "na"
    if result:
        print(result + " batman!")
    else:
        print("batman!")


if __name__ == '__main__':
    x = 6
    nanana_batman(x)

    x = 0
    nanana_batman(x)