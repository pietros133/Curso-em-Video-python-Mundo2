#Importação da Biblioteca datetime
from datetime import date
anonascimento=int(input("informe o ano em que você nasceu"))
atual = date.today().year
idade= atual - anonascimento
print("O Atleta tem: {} anos ".format(idade))
if idade <= 9:
    print("Classificação: Mirim")
elif idade > 9 and idade <= 14:
    print("Classificação: INFANTIL")
elif idade > 14 and idade <=19:
    print("Junior")
elif idade > 19 and idade <=25:
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("Classificação: MASTER")
else:
    exit()



