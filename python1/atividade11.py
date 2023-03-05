#fatorial de um número


n = int(input("Digite um número natural: "))
fatorial = 1
i = 2
while i <= n:
    fatorial *= i
    i += 1
print(f"{n}! = {fatorial}")
