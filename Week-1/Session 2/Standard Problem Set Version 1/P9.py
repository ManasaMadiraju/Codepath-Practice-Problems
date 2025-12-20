'''Write a function merge_alternately() that accepts two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.'''

def merge_alternately(word1, word2):
    final_word = ''
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            final_word += word1[i]
        if i < len(word2):
            final_word += word2[i]
    return final_word


if __name__ == '__main__':
    word1 = "wol"
    word2 = "oze"
    print(merge_alternately(word1, word2))

    word1 = "hfa"
    word2 = "eflump"
    print(merge_alternately(word1, word2))

    word1 = "eyre"
    word2 = "eo"
    print(merge_alternately(word1, word2))