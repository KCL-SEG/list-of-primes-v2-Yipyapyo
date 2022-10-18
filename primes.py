"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primeNumber(number):
    if number == 0 or number == 1:
        return False
    for x in range(2,number):
        if number % x == 0:
            return False
    else:
        return True
        
def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("The value you entered was below 0")
    else:
        list = []
        for i in range(number_of_primes):
            for x in range(2, 1000):
                if len(list) == number_of_primes:
                    pass
                else:
                    if primeNumber(x) == True:
                        list.append(x)
    return list