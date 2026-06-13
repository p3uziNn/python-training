print("Contador de números positivos, negativos e zeros")

# Criamos contadores para cada categoria
positivos = 0
negativos = 0
zeros = 0

# Loop que repete 8 vezes
for i in range(8):
    numero = float(input(f"Digite o {i + 1}º número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

# Exibimos os resultados
print(f"\nResultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
