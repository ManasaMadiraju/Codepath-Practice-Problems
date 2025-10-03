def find_villain(crowd, villian):
    result = []
    for key,value in enumerate(crowd):
        if value == villain:
            result.append(key)
    print(result)


if __name__ == '__main__':
    crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
    villain = 'The Joker'
    find_villain(crowd, villain)