#Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui
#ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, 
#imprima "não".

num = input("Digite um número inteiro: ")
i = 0
adj = False

while i < len(num) - 1 and not adj:
    if num[i] == num[i+1]:
        adj = True
    i += 1

if adj:
    print("sim")
else:
    print("não")
