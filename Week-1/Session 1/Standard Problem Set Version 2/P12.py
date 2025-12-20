'''Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].'''

def shuffle(cards):
    result = []
    n = len(cards) // 2
    for i in range(n):
        result.append(cards[i])
        result.append(cards[i+n])
    print(result)


if __name__ == '__main__':
    cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
    shuffle(cards)

    cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
    shuffle(cards)

    cards = [10, 10, 2, 2]
    shuffle(cards)
