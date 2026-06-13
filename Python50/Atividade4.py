print("Aumento de salário")

salario = float(input("Digite o valor do salário para ver o aumento de 15%: "))
calc = salario * 0.15
total = salario + calc

print(f"Com um aumento de 15% do salário o total é R$ {total: .2}" )