#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos 
#deste número na saída

num = input("Digite um número inteiro: ")

soma = 0
for digito in num:
    soma += int(digito)

print("A soma dos dígitos do número é:", soma)
