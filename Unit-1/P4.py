def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    return None


if __name__ == '__main__':
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    print(get_item(items, x))

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    print(get_item(items, x))
