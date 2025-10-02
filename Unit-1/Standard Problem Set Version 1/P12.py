def locate_thistles(items):
    result = []
    for key,value in enumerate(items):
        if value == 'thistle':
            result.append(key)
    return result


if __name__ == '__main__':
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    print(locate_thistles(items))

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    print(locate_thistles(items))