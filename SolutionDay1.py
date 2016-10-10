def prime(digit):
    primes = []
    for m in range(1,digit):
        if all(m % i != 0 for i in range(2,m)):
            primes.append(m)
    return primes


def fibonacci(number):
    output = []
    a,b = 1,1
    for i in range(number-1):
        a,b = b,a+b
        output.append(a)
    return output
