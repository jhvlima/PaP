def ehPrimo(n):
    return [x for x in range(2, n) if n % x == 0] == []

if __name__ == "__main__":
    print(ehPrimo(980796))