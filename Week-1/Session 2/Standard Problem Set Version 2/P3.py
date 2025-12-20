'''Write a function remove_name() to keep Batman's secret identity hidden. The function accepts a list of names people and a string secret_identity and should return the list with any instances of secret_identity removed. The list must be modified in place; you may not create any new lists as part of your solution. Relative order of the remaining elements must be maintained.'''


def remove_name(people, secret_identity):
    # Iterate backwards
    for i in range(len(people) - 1, -1, -1):
        if people[i] == secret_identity:
            people.pop(i)
    return people


if __name__ == '__main__':
    people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
    secret_identity = 'Bruce Wayne'
    print(remove_name(people, secret_identity))
