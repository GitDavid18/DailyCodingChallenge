# array of integers
# first missing positive int
# linear time
# const space
def find_smallest_missing(numbers):
    found = [0] * len(numbers)
    # for i in range():
    # found = 0

    for num in numbers:
        if (num <= 0 or num > len(numbers)):
            continue
        found[num-1] = 1

    for i in range(len(found)):
        if found[i] == 0:
            return i + 1

    return len(numbers) + 1


print(str(find_smallest_missing([3, 4, -1, 1])) + ' expected 2')     # 2
print(str(find_smallest_missing([1, 2, 0])) + ' expected 3')         # 3
print(str(find_smallest_missing([-1, 2, 0])) + ' expected 1')        # 1
print(str(find_smallest_missing([5, 4, 2, 1])) + ' expected 3')      # 3
print(str(find_smallest_missing([5, 4, 3, 2, 1])) + ' expected 6')   # 6
print(str(find_smallest_missing([-1, -2, 7, 4, 3, 2, 1])) + ' expected 5')
