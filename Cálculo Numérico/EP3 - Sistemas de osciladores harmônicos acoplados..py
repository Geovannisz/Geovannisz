# Neste EP foi utilizado o metodo direto da eliminacao gaussiana.
# A escolha desse metodo foi devida a convergencia ser sempre possivel
# dado que omega deve ser diferente de omega0. Metodos iterativos aca-
# bam nos gerando inumeros problemas uma vez que o criterio das linhas
# eh facilmente desrespeitado. O programa funciona bem para N = 200,
# levando cerca de 3 segundos para plotar o resultado. Uma forma de
# melhorar este algoritmo seria evitar fazer operacoes desnecessarias
# dos inumeros zeros que a matriz possui, dado que os termos dela es-
# tao distribuidos apenas em torno da diagonal principal, diminuindo
# assim, o tempo de processamento do codigo.

import math

N = int(input());
omega = float(input());
omega0 = float(input());
a0 = float(input());

# funcao que define a matriz A

def Matriz_A(N,omega,omega0):
    
    # cria a matriz A como matriz nula
    
    A = []
    for x in range(N):
        linha = []
        for y in range(N):
            linha.append(0)
        A.append(linha)
        
    # constroi a matriz A dada as condicoes do problema
    
    for i in range(N):
        
        # primeira linha
        if i == 0:
            A[i][i] = omega0**2 - omega**2
            A[i][i+1] = -omega0**2
            
        # ultima linha
        elif i+1 == N:
            A[i][i-1] = -omega0**2
            A[i][i] = omega0**2 - omega**2
            
        # todas as linhas com excessao da primeira e da ultima
        else:
            A[i][i-1] = -omega0**2
            A[i][i] = 2*omega0**2 - omega**2
            A[i][i+1] = -omega0**2
        
    return A
    
# funcao que aplica o metodo e retorna a matriz dvec

def Eliminacao_de_Gauss(A,a0):
    
    N = len(A[0])  # define quantas linhas e colunas a matriz tem
    
    # cria a matriz b
    
    b = []
    for a in range(N):
        b.append(0)
    b[0] = a0        # primeiro termo da matriz b dado
    
    # acessar as linhas
    
    for i in range(N):
        
        # verifica qual eh o maior pivo
        
        pivo = math.fabs(A[i][i])
        i_pivo = i
        for j in range(i+1,N):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                i_pivo = j
                
        # permuta as linhas (troca numero de i para i_pivo)
        
        if i_pivo != i:
            i_auxiliar = A[i]       # salva o valor de A[i]
            A[i] = A[i_pivo]
            A[i_pivo] = i_auxiliar
            b_auxiliar = b[i]       # salva o valor de b[i]
            b[i] = b[i_pivo]
            b[i_pivo] = b_auxiliar
            
        # eliminação gaussiana
        
        for m in range(i+1,N):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i,N):
                A[m][n] = A[m][n] - multiplicador*A[i][n]
            b[m] = b[m] - multiplicador*b[i]
            
    # cria a matriz dvec
            
    dvec = []
    for a in range(N):
        dvec.append(0)
        
    # encontra os valores de dvec
        
    i = N - 1
    while i >= 0:    # encontra os valores da ultima ate a primeira linha
        d = b[i]
        j = N - 1
        while j > i:   # j deve ser maior que i pois A ja esta escalonada
            d = d - A[i][j]*dvec[j]
            j = j - 1
        d = d/A[i][i]
        i = i - 1
        dvec[j] = d
        
    return dvec

A = Matriz_A(N,omega,omega0)      # atribui matriz A criada

dvec = Eliminacao_de_Gauss(A,a0)  # encontra dvec pela eliminacao gaussiana

for num in dvec:
     print("{:8.4f}".format(num))