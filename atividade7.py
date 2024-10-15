#  Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada. 


# f=0.5555555555555556
# c=1.8

while (True):
    selecao = input("Conversão de °C ou °F:")
    if selecao =="c" or selecao =="C" or selecao == "celsius":
        temperatura = float(input("Adicione para conversão:"))
        c=0.5555555555555556 * temperatura - 32
        print(f"a temperatura é {c}")
    elif selecao =="f" or selecao == "F" or selecao == "Fahrenheit":
        temperatura = float(input("Adicione para conversão:"))
        f=1.8 * temperatura + 32
        print(f"a temperatura é {f}")
    elif selecao == "sair" or selecao == "quit":
        quit()

    else:
        print("Coloque F ou C(ou escreva corretamente os nomes)")
