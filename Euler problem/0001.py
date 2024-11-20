# If we list all the natural numbers below that are multiples of or , we get and . The sum of these multiples is.

# Find the sum of all the multiples of or below .

 

def sum_in_range(max):
    sum = 0 
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_in_range(10))
print(sum_in_range(1000))
    