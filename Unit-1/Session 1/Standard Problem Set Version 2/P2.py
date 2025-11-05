'''Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".'''

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")


if __name__ == '__main__':
    verb = "give up"
    madlib(verb)

    verb = "nap"
    madlib(verb)