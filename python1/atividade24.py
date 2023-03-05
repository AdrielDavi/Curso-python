#Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 
#2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, 
#se for o caso, n).

def n_primos(n):
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            count += 1
    
    return count
