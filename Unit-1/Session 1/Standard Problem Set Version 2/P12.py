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
