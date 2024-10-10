def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Adicione o número:"))
if numero > 0:
        print(f"O fatorial de {numero} é {fatorial(numero)}")
else:
     print("adicione um número acima de 0")

