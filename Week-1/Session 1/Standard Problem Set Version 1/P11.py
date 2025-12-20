'''Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.'''

def tiggerfy(s):
    stolen = 'tiger'
    result = ''

    for ch in s:
       if ch.lower() not in stolen:
           result+=ch
    return result


if __name__ == '__main__':
    s = "suspicerous"
    print(tiggerfy(s))

    s = "Trigger"
    print(tiggerfy(s))

    s = "Hunny"
    print(tiggerfy(s))

