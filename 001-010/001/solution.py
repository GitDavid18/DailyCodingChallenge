def containsSum(sum, numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if sum == numbers[i] + numbers[j]:
                return True
    return False


print(containsSum(1, [1, 2, 3, 4]))
print(containsSum(3, [1, 2, 3, 4]))
print(containsSum(5, [1, 2, 3, 4]))
print(containsSum(7, [1, 2, 3, 4]))
print(containsSum(9, [1, 2, 3, 4]))
