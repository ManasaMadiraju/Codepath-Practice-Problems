'''Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that contains the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.'''

def exclusive_elemts(lst1, lst2):
    return list(set(lst1) ^ set(lst2))


if __name__ == '__main__':
    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["piglet", "eeyore", "owl"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["pooh", "roo", "piglet"]
    print(exclusive_elemts(lst1, lst2))