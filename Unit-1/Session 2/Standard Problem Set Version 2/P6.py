'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases and more than once.

'''

def reverse_vowels(s):
    vowel_list = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s)-1

    while left<right:
        if s[left] not in vowel_list:
            left += 1
        elif s[right] not in vowel_list:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)


if __name__ == '__main__':
    s = "robin"
    print(reverse_vowels(s))

    s = "BATgirl"
    print(reverse_vowels(s))

    s = "batman"
    print(reverse_vowels(s))