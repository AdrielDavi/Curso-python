#Segue abaixo um programa em Python que recebe um número inteiro na entrada e imprime "Buzz" se o número 
#for divisível por 5, ou imprime o mesmo número que foi dado na entrada caso contrário:

numero = int(input("Digite um número inteiro: "))

if numero % 5 == 0:
    print("Buzz")
else:
    print(numero)
