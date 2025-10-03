def linear_search(items, target):
    for key,value in enumerate(items):
        if value == target:
            return key
    return -1
    


if __name__ == '__main__':
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))