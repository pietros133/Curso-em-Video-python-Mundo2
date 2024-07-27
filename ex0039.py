#Entrada de Dados
ano=int(input("Digite o Ano em que você nasceu:  "))
# Calc = Calculo
calc= (2024 - ano)
#Inicio das Condições
#Verificar se o Resultado de Calc é igual a 18
if calc == 18:
    print("Você Já  Deve se Alistar")
 # Verificar se o Resultado de Calc é Menor que 18
elif calc < 18:
    print("Você ainda não deve se Alistar, faltam {} anos".format(18-calc))
# Verificar se o Resultado de Calc é Maior que 18
elif calc > 18:
    print("\033[;;31mVOCÊ JÁ DEVERIA TER SE ALISTADO!, PASSARAM {} ANOS".format(calc-18))
else:
    exit()

