'''Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.'''

 #Approach 1
def expose_superman(trust, n):
    if n == 1:
        return 1

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for a, b in trust:
        out_degree[a] += 1
        in_degree[b] += 1

    for person in range(1, n + 1):
        if out_degree[person] == 0 and in_degree[person] == n - 1:
            return person

    return -1

#Approach 2
#def expose_superman(trust, n):
    # population = set()
    # hashmap = {}
    # possible_supermans = []
    # for i in trust: #[1,3]
    #     hashmap[i[0]] = i[1]
    #     population.add(i[0])
    #     population.add(i[1])
    # for value in population:
    #     if value not in hashmap.keys():
    #         possible_supermans.append(value)

    # trusted_people = list(hashmap.values())
    # for superman in possible_supermans:
    #     if trusted_people.count(superman) == n - 1:
    #         return superman   
    # return -1

if __name__ == '__main__':
    n = 2
    trust = [[1, 2]]
    print(expose_superman(trust, n))

    n = 3
    trust = [[1, 3], [2, 3]]
    print(expose_superman(trust, n))

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(expose_superman(trust, n))
