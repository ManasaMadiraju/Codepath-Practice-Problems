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

