r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    # end = ' ' Caso não queira Quebrar a linha
    print("Os Segmentos acima podem formar um triangulo ",end=' ')

    if  r1 == r2 == r3:
           print('Equilatero')
           # Diferente em Python !=
    elif  r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("Os Segmentos acima não podem formar um triangulo")
