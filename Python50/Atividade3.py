print("Desconto do produto")

preço = float(input("Digite o valor desejado para saber com 10 porcento de desconto: "))
calc = preço * 0.10
total = preço - calc

print(f"O valor com 10% de desconto é R$ {total: .2f}")