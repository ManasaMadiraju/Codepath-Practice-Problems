'''Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list of the elements that are common to both lists.'''


def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))


if __name__ == '__main__':
    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["super speed", "time travel", "dimensional travel"]
    print(common_elements(lst1, lst2))

    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["martial arts", "stealth", "master detective"]
    print(common_elements(lst1, lst2))