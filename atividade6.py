# Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).

def ordenar(numeros):
    return sorted(numeros)

numeros = []
for x in range(5):
    numeros.append(int(input("Adicione os números:")))

numeros_ordenados = ordenar(numeros)

print("Em ordem:", numeros_ordenados)