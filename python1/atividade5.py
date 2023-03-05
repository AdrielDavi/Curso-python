#programa em Python que recebe um número inteiro na entrada e imprime "Fizz" se o número for 
#divisível por 3, ou imprime o mesmo número que foi dado na entrada caso contrário:

numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0:
    print("Fizz")
else:
    print(numero)
