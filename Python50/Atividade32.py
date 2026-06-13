print("Descubra seu IMC ")
peso = float (input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC =  peso / (altura * altura) 

if IMC <= 18.5:
    print("você está abaixo do peso, procure um nutricionista")
elif IMC <= 24.9:
    print("você está como o peso normal, parábens")
elif IMC <= 29.9:
    print("excesso de peso, dá uma maneirada na comida")
elif IMC <= 30:
    print("Paraaaa de cumê, IMENSO kkkkkkkk")
elif IMC <= 35:
    print("Não vai ter caixão que lhe caiba meu amigo kkkkkkkkkkkk") 