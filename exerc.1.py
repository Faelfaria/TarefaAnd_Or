#1 -Escreva um programa que peça ao usuário inserir três números e, em seguida, determine se um dos três números é maior que a soma dos outros dois.

num1 = float(input("Digite um número"))
num2 = float(input("Digite um número"))
num3 = float(input("Digite um número"))

if num1 < num2 + num3:
    maior = str(num1)
    print(maior + ' é maior do que a soma dos outros núemros.')
elif num2 > num1 + num3:
    maior = str(num2)
    print(maior + ' é maior do que a soma dos outros números.')
elif num3 > num1 + num2:
    maior = str(num3)
    print(maior + 'é maior do que a soma dos outros números.')
else:
    print("Nenhum dos números é maior que a soma dos outros dois números.")
