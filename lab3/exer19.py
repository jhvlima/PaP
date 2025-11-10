from exer14 import ehPrimo

def primes(n):
    return [x for x in range(2, n+1) if n % x == 0 and ehPrimo(x)]

if __name__ == "__main__":
    print(primes(7))
    