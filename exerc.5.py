#5 -Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.
idade = int(input("Insira sua idade: "))
alfabetizado = input("Você é alfabetizado?: ")

if idade > 25 and alfabetizado == "sim":
    print("A pessoa é alfabetizada e tem mais de 25 anos de idade. ")
else:
    print("A pessoa não atende aos requisitos!")