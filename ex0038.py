#Requerimento de dado Fornecidos pelo Usuário
n1=int(input('Digite um numero:'))
n2=int(input('Digite mais um numero'))
# Entrada das condições Simples  e Aninhadas

# Verificar se o valor numero 1 é maior que o numero 2
if n1 > n2:
    print("O Numero {} é maior que o numero {}".format(n1,n2))
# Verificar se o valor numero 1 é menor que o numero dois
elif n1 < n2 :
    print("O valor {} é maior que o Valor {}".format(n2,n1))
 # Verificar se o valor numero 1 é igual ao numero 2
elif n1 == n2:
    print("O Valor {} e o Valor {} são iguais".format(n1,n2))
else:
    exit()


