'''T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.'''

def tiggerfy(word):
    sub = ['t','i','gg','er']
    lower_word = word.lower()

    for s in sub:
        lower_word = lower_word.replace(s,'')
    return lower_word
    

if __name__ == '__main__':
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))
