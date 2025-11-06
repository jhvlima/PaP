from exer1 import head
from exer2 import tail

def maioresQueN(lista, n):
    if lista == []:
        return 0
    if n < head(lista):
        return 1 + maioresQueN(tail(lista), n)
    else: 
        return maioresQueN(tail(lista), n)

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    print(maioresQueN(lista, n))
