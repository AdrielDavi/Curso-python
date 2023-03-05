#Receba um número inteiro positivo na entrada e imprima os 

#n primeiros números ímpares naturais.


n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("O número precisa ser positivo.")
else:
    count = 0
    num = 1
    while count < n:
        if num % 2 != 0:
            print(num)
            count += 1
        num += 1
