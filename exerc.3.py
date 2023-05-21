#3 -Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.
idade = int(input("Informe sua idade: "))
autorização = input("Tem autorização dos pais?: ")

if idade >= 18 or autorização == "sim":
    print("Você pode entrar! ")
else:
    print("Você não pode entrar! ")