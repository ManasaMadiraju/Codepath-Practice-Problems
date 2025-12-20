'''Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.'''

def doubled(hunny_jars):
    doubled = [i*2 for i in hunny_jars]
    print(doubled)


if __name__ == '__main__':
    hunny_jars = [1, 2, 3]
    doubled(hunny_jars)