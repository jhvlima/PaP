from exer11 import inverteLista
from exer6 import catListas

def geraPalindromo(lista):
    return catListas(lista, inverteLista(lista)) 

if __name__ == "__main__":
    print(geraPalindromo(list("abcd")))