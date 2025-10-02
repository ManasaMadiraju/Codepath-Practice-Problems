def print_catchphrase(character):
    hashmap = {"Pooh": "Oh bother!", "Tigger": "TTFN: Ta-ta for now!", "Eeyore": "Thanks for noticing me.", "Christopher Robin" : "Silly old bear."}

    if character in hashmap:
        print(hashmap[character])
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


if __name__ == '__main__':
    character = "Pooh"
    print_catchphrase(character)

    character = "Piglet"
    print_catchphrase(character)
