from exer1 import head
from exer2 import tail

def catListas(lista1, lista2):
    if lista2 == []:
        return lista1
    return catListas(lista1 + [head(lista2)], tail(lista2))

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(catListas(lista1, lista2))