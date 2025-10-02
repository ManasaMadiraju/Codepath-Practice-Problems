def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity+1):
        if quantity % i == 0:
            divisors.append(i)
    print(divisors)


if __name__ == '__main__':
    quantity = 6
    split_haycorns(quantity)

    quantity = 1
    split_haycorns(quantity)







