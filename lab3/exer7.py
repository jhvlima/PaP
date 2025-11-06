from exer1 import head
from exer2 import tail

def temElemento(lista, elemento):
    if lista == []:
        return False
    if head(lista) == elemento:
      return True
    else:
      return temElemento(tail(lista), elemento)

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    elemento = 5
    print(temElemento(lista, elemento))