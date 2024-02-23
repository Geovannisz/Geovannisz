Npol=int(input())  # Pede o grau do polinomio
Ndata=int(input()) # Pede o número de pontos
xdata = []
ydata = []
tabela = []
for ii in range(Ndata):  # pede e armazena os pontos em xdata e ydata
    x = float(input())
    y = float(input())
    xdata.append(x)
    ydata.append(y)
tabela.append(ydata)  # tabela que armazena valores de f(x) e de todas as diferenças divididas

xbar = []
for k in range(0,Ndata-1):  # encontra todos os valores medios de x
    x_k = (xdata[k+1] + xdata[k])/2
    xbar.append(x_k)

passo = 1
for n in range(Npol):              # repete enquanto a ordem for menor do que Npol
    grau = []                       # separa as diferenças divididas pelo grau de interpolacao
    for m in range(len(tabela[n])-1):  # encontra as diferenças divididas e armazena os valores na tabela
        f = (tabela[n][m+1] - tabela[n][m])/(xdata[m+passo] - xdata[m])
        grau.append(f)
    tabela.append(grau)     # adiciona uma lista de todas as diferenças divididas calculadas a tabela
    passo = passo + 1

def polinomio(x,xdata,tabela,Npol):  # constroi um polinomio e encontra o valor dele para um dado x
    polinomio = 0
    for i in range(Npol + 1):       # repete enquanto nao tiver multiplicado pelo termo de ultimo grau Npol
        fator = tabela[i][0]       # escolhe apenas o primeiro termo de cada grau da tabela, sendo f(x0),df[x,x0],d^2f[x,x0,x1]...
        for j in range(i):
            fator = fator*(x-xdata[j])   # multiplica o primeiro termo de cada grau da tabela por (x-x0)*(x-x1)*...(x-xj)
        polinomio = polinomio + fator    # soma o novo fator ao valor do polinomio
    return polinomio

yNewton = []   # lista que armazenara os valores de p_n(x_k)

for k in range(Ndata-1):
    x = xbar[k]    # escolhe o valor de x para substituir no polinomio
    yNewton.append(polinomio(x,xdata,tabela,Npol))   # calcula o polinomio

for ii in range(Ndata-1):     # imprime o que esta sendo pedido
     print("{:10.6e}".format(xbar[ii]))
     print("{:10.6e}".format(yNewton[ii]))