#  Faça um Programa que peça as 4 notas bimestrais e mostre a média.  Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Calcular média do aluno (FHA)")

ESCOLA = str ("FHA")

nome = input("Digite o nome do aluno: ")

nota1 = int (input("digite a primeira nota:"))
nota2 =int (input("digite segunda a nota: "))
nota3 = int (input("digite terceira a nota: "))
nota4 = int (input("digite quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) /4

if media >= 6:
    print(f"O aluno {nome} foi aprovado e sua média é {media}")
elif media == 7.0:
    print("7? é o robozão pae? kkkk")
else:
    print("reprovou paizão, quer fazer a recuperação?")

print(f"O aluno(A) {nome} da escola {ESCOLA} ficou com a média {media}")


