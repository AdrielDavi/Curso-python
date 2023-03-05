#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de 
#vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados 
#recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas 
#diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido
#para número, pode ser tratado como texto


x = input("Digite o nome do cliente:")
y = input("Digite o dia de vencimento:")
z = input("Digite o mês de vencimento:")
k = input("Digite o valor da fatura:")

print("Olá",x)
print("A sua fatura com vencimento em ",y," de ",z," no valor de R$ ",k, " está fechada.")