# The prime factors of are and.

# What is the largest prime factor of the number 600851475143?

#Answer: 71 x 839 x 1471 x 6857

def get_primefactors(number):
    factors = []
    while(number > 1):
        curHighest = 2
        for i in range(curHighest, number + 1):    
            if number % i == 0:
                number =int( number / i)
                factors.append(i)
                curHighest = i
                break
        
    return factors


factors = (get_primefactors(600851475143))
print(factors)
print(max(factors))

print(get_primefactors(8))
print(get_primefactors(256))
print(get_primefactors(1000))
print(get_primefactors(27))
print(get_primefactors(2712357125))