print("Calculadora de média")
aluno= str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
media = (nota1 + nota2 + nota3) /3

if media >=7:
    print(f"O aluno {aluno} foi aprovado com nota {media:.2f}")
elif media <5:
    print(f"O aluno {aluno} foi reprovado direto com a nota {media:.2f}")
else:
    print(f"O aluno {aluno} está de recuperação com a nota {media:.2f}")
    notarecupera = float(input("Digite a nota da recuperação do aluno: "))

    media_final = (media + notarecupera) /2

    if media_final >=6:
        print(f"O aluno {aluno} foi aprovado na recuperação com a nota {media_final:.2f}")
    else:
        print(f"O aluno {aluno} foi reprovado na recuperação com a nota {media_final:.2f}")  