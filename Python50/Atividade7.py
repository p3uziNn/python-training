print("Peça um número ao usuário e diga se ele é par ou ímpar.")

numero = int(input("Digite o numero desejado: "))
verificador = numero % 2

if verificador == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar ")