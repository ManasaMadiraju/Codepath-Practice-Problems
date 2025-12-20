'''Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or subtract 1 from any element of nums. Return the minimum number of operations to make all elements of nums divisible by 3.'''

def make_divisible_by_3(nums):
    ops = 0

    for n in nums:
        if n % 3 != 0:
            ops += 1
    return ops


if __name__ == '__main__':
   nums = [1, 2, 3, 4]
   print(make_divisible_by_3(nums))

   nums = [3, 6, 9]
   print(make_divisible_by_3(nums))
