#Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo 
#n e devolva a soma de todos os inteiros entre 1 e 
#n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.


def eh_hipotenusa(n):
    """Verifica se um número é hipotenusa de algum triângulo retângulo com catetos inteiros."""
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) ** 0.5
            if c == int(c):
                return True
    return False

def soma_hipotenusas(n):
    """Retorna a soma de todas as hipotenusas de triângulos retângulos com catetos inteiros entre 1 e n."""
    soma = 0
    for i in range(1, n+1):
        if eh_hipotenusa(i):
            soma += i
    return soma
print(soma_hipotenusas(25))