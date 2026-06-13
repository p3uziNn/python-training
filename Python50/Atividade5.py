print("Verificação de vogal ou consoante:")
vogal = "A", "E", "I", "O", "U", 

letra = str(input("Digite a letra para saber se é vogal ou consoante:"))

if letra.upper() in vogal: 
    print(f"A letra {letra} é uma vogal: ")
else:
    print(f"A Letra {letra} é uma consoante")