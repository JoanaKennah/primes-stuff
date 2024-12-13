def pi_euler2(n):
    primes = [3,5,7,11,13,17,19,23,29,31]
    dividers = [4,4,8,12,12,16,20,24,28,32]
    total = 1 + (1 / 2)
    if n > 2:
        for i in range(n):
            if i in primes:
                if i == (dividers[i] - 1): # if i is a prime in the form 4m - 1 then positive
                    total = total + (1 / i)
                elif i == (dividers[i] + 1): # if i is a prime in the form 4m + 1 then negative
                    total = total - (1 / i)
            else:
                pass
                #prime_decompisition = []
        return total
    else:
        return total

print(pi_euler2(10))

    # if composite number then the sign is whatever the prime decomposisition sign is