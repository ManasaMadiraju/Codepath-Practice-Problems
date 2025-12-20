'''Write a function move_zeroes that accepts an integer array nums and returns a new list with all 0s moved to the end of list. The relative order of the non-zero elements in the original list should be maintained.'''

def move_zeroes(lst):
    new_list = []
    count = 0
    for n in lst:
        if n != 0:
            new_list.append(n)
        else:
            count += 1
    while count > 0:
        new_list.append(0)
        count -= 1
    return new_list


if __name__ == '__main__':
    lst = [1, 0, 2, 0, 3, 0]
    print(move_zeroes(lst))

