d=float(input())     # numero decimal
dint=int(d)          # parte inteira
dfloat=d-dint        # parte fracionaria
bn=[]                # lista para os numeros

while dint>0:
    b=dint%2         # resto da divisao -> numero binario
    dint=dint//2     # divisao inteira para o proximo numero
    bn.insert(0,b)   # insere numero binario no inicio
    
bn.append('.')       # adiciona um ponto para separar a parte inteira da fracionaria

i=0                  # variavel para terminar a repeticao
if dfloat!=0:        # se a parte fracionaria existir
    while i<15:      # o numero max de numeros a direita do ponto e 15
        dfloat*=2         # multiplica a parte fracionaria por 2
        if dfloat>1:
            bn.append(1)      # parte inteira
            dfloat=dfloat-1   # se a parte fracionaria for maior que 1, deve-se subtrair 1
            i+=1              # para ir para a proxima casa binaria
        elif dfloat==1:
            bn.append(1)      # se a parte fracionaria for 1, a parte inteira sera 1
            i=15              # finaliza a repeticao, pois a parte fracionaria chega a 1
        else:
            bn.append(0)      # se a parte fracionaria for menor que 1, a parte inteira e 0
            i+=1              # para ir para a proxima casa binaria
    print(*bn,sep="")         # imprime numero binario com a parte inteira e fracionaria

else:                         # se a parte fracionaria nao existir
    print(*bn,sep="")         # imprime numero binario com a parte inteira