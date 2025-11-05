def final_value_after_operations(operations):
    tigger = 1
    hashmap = {'bouncy':1,'flouncy':1,'trouncy':-1,'pouncy':-1}
    for i in operations:
        if i in hashmap:
            tigger += hashmap[i]
    return tigger



if __name__ == '__main__':
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))