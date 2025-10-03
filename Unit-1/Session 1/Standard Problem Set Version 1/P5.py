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

