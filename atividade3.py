palavra = str(input("adicione uma palvra:"))
inverter = palavra[::-1]
if inverter == palavra:
    print("é um palindromo")
else:
    print("não é um palindromo")
