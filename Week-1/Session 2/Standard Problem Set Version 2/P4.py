'''Given a non-negative integer n, write a function count_digits() that returns the number of digits in n. You may not cast n to a string.

'''

def count_digits(n):
    #with casting
    # n =  len(list(map(int,str(n)))) 
    # return n

    #without typecasting str
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10 #Floor Division
        count += 1
    return count




if __name__ == '__main__':
    n = 964
    print(count_digits(n))

    n = 0
    print(count_digits(n))