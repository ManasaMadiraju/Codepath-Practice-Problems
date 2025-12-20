'''Implement a function count_evens() that accepts a list of strings lst as a parameter. The function should return the number of strings with an even length in the list.'''

def count_evens(lst):
    count = 0
    for s in lst:
        if len(s) % 2 == 0:
            count += 1
    return count


if __name__ == '__main__':
    lst = ["na", "nana", "nanana", "batman", "!"]
    print(count_evens(lst))

    lst = ["the", "joker", "robin"]
    print(count_evens(lst))

    lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
    print(count_evens(lst))