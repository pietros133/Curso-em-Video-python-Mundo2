#Declaração das Variaveis
n1=float(input("Digite a Primeira Nota: "))
n2=float(input("Digite a segunda Nota:"))
# Calculo da Média
media=(n1+n2)/2
# Verifica se o resultado da Média é menor que Cinco
if media < 5:
    print("Estudar Mais, REPROAVADO")
# Verifica se o resultado da média é maior que Cinco e menor que Sete
elif 7 > media >= 5:
 print("ESTUDAR MAIS RECUPERAÇÃO")
 # Verifica se o resultado da média é maior que Sete
elif media >= 7:
    print("Parabéns, Você foi APROVADO")
else:
    print("TU NEM É ALUNO")
exit()


