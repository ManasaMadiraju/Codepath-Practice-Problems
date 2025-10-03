# Approach 1
def concatenate(words):
    concatenated = ''
    for s in words:
        concatenated += s
    print(concatenated)

# Approach 2
def concatenate(words):
    print("".join(words))

if __name__ == '__main__':
    words = ["vengeance", "darkness", "batman"]
    concatenate(words)

    words = []
    concatenate(words)