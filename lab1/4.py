n = int(input())
soma = 0

while n > 9:
    soma += n%10
    n = n//10

soma += n
print(soma)
