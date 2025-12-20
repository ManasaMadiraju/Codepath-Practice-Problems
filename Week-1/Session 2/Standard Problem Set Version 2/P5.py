'''Write a function move_zeroes that accepts an integer array nums and returns a new list with all 0s moved to the end of list. The relative order of the non-zero elements in the original list should be maintained.'''

def move_zeroes(lst):
    non_zeros = []
    zero_count = 0

    for n in lst:
        if n == 0:
            zero_count += 1
        else:
            non_zeros.append(n)
    return non_zeros + [0] * zero_count


if __name__ == '__main__':
    lst = [1, 0, 2, 0, 3, 0]
    print(move_zeroes(lst))

