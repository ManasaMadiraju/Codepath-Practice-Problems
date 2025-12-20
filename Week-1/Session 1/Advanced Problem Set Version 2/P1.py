'''Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices representing the words that contain the character x. The returned list may be in any order.'''

def words_with_char(words, x):
    result = []
    for key, value in enumerate(words):
        if x in value:
            result.append(key)
    return result

if __name__ == '__main__':
    words = ["batman", "superman"]
    x = "a"
    print(words_with_char(words, x))

    words = ["black panther", "hulk", "black widow", "thor"]
    x = "a"
    print(words_with_char(words, x))

    words = ["star-lord", "gamora", "groot", "rocket"]
    x = "z"
    print(words_with_char(words, x))