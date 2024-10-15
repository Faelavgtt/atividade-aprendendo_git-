# Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.

def fibonacci(n):
    a,b=0,1
    sequencia = []

    for x in range(n):
        sequencia.append(a)
        a,b = b,a + b
    return sequencia

n = int(input("informe o número:"))
if n <=0:
    print("Informe um número positivo.")
else:
    print(f"os `{n} primeiros termos da sequencia de fibonacci são:{fibonacci(n)}")