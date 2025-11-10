from exer14 import ehPrimo

def proximoPrimo(n):
    if ehPrimo(n+1):
        return n+1
    return proximoPrimo(n+1)

if __name__ == "__main__":
    print(proximoPrimo(2))