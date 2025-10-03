def up_and_down(lst):
    odd, even = 0, 0
    for n in lst:
        if n%2 != 0:
            odd += 1
        else:
            even += 1
    print(odd-even)


if __name__ == '__main__':
    lst = [1, 2, 3]
    up_and_down(lst)

    lst = [1, 3, 5]
    up_and_down(lst)

    lst = [2, 4, 10, 2]
    up_and_down(lst)

