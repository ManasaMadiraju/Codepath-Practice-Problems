'''Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.'''

def find_villain(crowd, villain):
    result = []
    for key,value in enumerate(crowd):
        if value == villain:
            result.append(key)
    return result


if __name__ == '__main__':
    crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
    villain = 'The Joker'
    print(find_villain(crowd, villain))