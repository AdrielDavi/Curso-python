#escreva um programa que calcula as raízes de uma equação do segundo grau.

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Esta equação não possui raízes reais.")
elif delta == 0:
    raiz = (-b + delta**0.5) / (2*a)
    print(f"A raiz dupla desta equação é {raiz:.1f}.")
else:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    if raiz1 < raiz2:
        print(f"As raízes da equação são {raiz1:.1f} e {raiz2:.1f}.")
    else:
        print(f"As raízes da equação são {raiz2:.1f} e {raiz1:.1f}.")
