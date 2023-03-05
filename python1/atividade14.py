#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
#Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int(input("Digite um número inteiro positivo: "))

# verificando se o número é menor que 2
if numero < 2:
    print("Não primo")
else:
    # verificando se o número é divisível por algum número entre 2 e a metade dele mesmo
    for i in range(2, numero//2 + 1):
        if numero % i == 0:
            print("Não primo")
            break
    else:
        print("Primo")
