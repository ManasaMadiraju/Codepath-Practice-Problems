def get_odds(nums):
    odds = []
    for n in nums:
        if n%2 != 0:
            odds.append(n)
    print(odds)


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    get_odds(nums)

    nums = [2, 4, 6, 8]
    get_odds(nums)