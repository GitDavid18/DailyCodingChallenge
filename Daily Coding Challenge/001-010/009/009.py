# biggest sum of non adjacent nums
# can be 0 or neg
# O(n) time and const space?

def biggestSum(numbers):
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]
    biggest = 0
    for i in range(len(numbers) - 1):
        if i+1 >= len(numbers) - 1:
            return max(numbers[i:])
        return max(numbers[i] + biggestSum(numbers[i+2:]), biggestSum(numbers[i+1:]))


one = [3]
result = biggestSum(one)
print(result)
assert biggestSum(one) == 3

two = [2, 3]
result = biggestSum(two)
print(result)
assert biggestSum(two) == 3

first = [2, 4, 6, 2, 5]
result = biggestSum(first)
print(result)
assert biggestSum(first) == 13

second = [5, 1, 1, 5]
result = biggestSum(second)
print(result)
assert result == 10

another = biggestSum([2, 4, 1, 1, 2])
print(another)
assert another == 6

assert biggestSum([2, 4, 6, 8]) == 12
