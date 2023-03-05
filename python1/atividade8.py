#programa em Python que recebe três números inteiros na entrada e imprime "crescente" se eles estiverem 
#em ordem crescente, ou imprime "não está em ordem crescente" caso contrário:





a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a < b < c:
    print("crescente")
else:
    print("não está em ordem crescente")
