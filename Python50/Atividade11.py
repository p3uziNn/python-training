print("Calculadora de média de 10 números")

# Começamos com a variável que vai acumular a soma dos números
soma = 0

# Usamos um laço for para repetir 10 vezes
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))  # Pede um número ao usuário
    soma += numero  # Adiciona esse número à soma total

# Depois do laço, calculamos a média
media = soma / 10

# Mostramos o resultado formatado com 2 casas decimais
print(f"A média dos 10 números é: {media:.2f}")

    