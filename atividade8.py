# Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados.

# def maior_menor():
numeros = []

for i in range(5):
    numero = int(input("Adicione o número: "))
    numeros.append(numero)
menor = maior = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print("Menor número:", menor)
print("Maior número:", maior)