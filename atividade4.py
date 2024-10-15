#Faça um programa que verifique se um número fornecido é primo.
def primo():
    numero=int(input("adicione um número:"))

    if numero < 2:
        print(numero, "não é um número primo.")
        return

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(numero,"não é um número primo.")
            return
    
    print(numero,"é um número primo.")
primo()
    

    
