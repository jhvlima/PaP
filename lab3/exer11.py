from exer1 import head
from exer2 import tail
from exer6 import catListas

def inverteLista(lista):
    if lista == []:
        return []
    return catListas(inverteLista(tail(lista)), [head(lista)])

if __name__ == "__main__":
    print (inverteLista([1,2,3,4]))