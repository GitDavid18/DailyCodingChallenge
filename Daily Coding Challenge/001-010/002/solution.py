def productOfOthers(numbers):
    if len(numbers) == 0:
        return 0

    output = []
    product = 1
    for i in numbers:
        product *= i

    for i in range(len(numbers)):
        output.append(product / numbers[i])

    return output


def bonus_productOfOthersNoDivision(numbers):
    if len(numbers) == 0:
        return 0
    output = []
    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if i == j:
                continue
            product *= numbers[j]
        output.append(product)

    return output


print(productOfOthers([]))
print(bonus_productOfOthersNoDivision([]))
print(productOfOthers([1, 2, 3, 4, 5]))
print(bonus_productOfOthersNoDivision([1, 2, 3, 4, 5]))
