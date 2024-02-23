# Neste ep foi utilizado o metodo de Newton.
# Para que haja convergencia, foi feita uma analise grafica da funcao.
# Assim, foi observado que a funcao possui assintotas
# localizadas em Zn = (2n-1)*pi/2 onde n = 1,2,3...
# Assim, o metodo de newton ira convergir os casos onde
# Zn = (2n-1)*pi/2 - (um numero muito pequeno)
# Portanto, podemos calcular os 3 chutes iniciais
# ------------------------------------
# Problemas deste metodo nesta funcao:
# ------------------------------------
# Para valores maiores do que 10000pi (muito grandes)
# O chute inicial nao converge para a raiz
# -----------------------
# Vantagens deste metodo:
# -----------------------
# Convergencia quadratica (rapida)

import math

Zm = float(input())

def f(x):    # define a funcao f(x)
    return math.tan(x)-math.sqrt(((Zm/x)**2)-1)

def Df(x):   # define a derivada da funcao f(x)
    return ((Zm**2)/(math.sqrt(((Zm/x)**2)-1)))+(1/(math.cos(x))**2)

xn = []      # lista para os 3 chutes iniciais
for n in range(1,4):
    zn = (2*n-1)*(math.pi/2)  # serie das assintotas
    xn.append(zn-0.0001)    # correcao de 0.0001 para convergencia

def funcao(xn,Zm):   # calcula o metodo de newton para os 3 chutes iniciais
    raizes = []      # lista para as raizes apos a convergencia
    x1 = 0
    for b in range(0,len(xn)):
        x = xn[b]
        while abs(x - x1) >= 0.00000001:  # precisao suficiente grande para que a convergencia seja boa até a casa de 10^-4
            x1 = x    # avanca para a proxima iteracao
            x = x1 - f(x1)/Df(x1)   # metodo de newton
        raizes.append(x)  # adiciona raiz calculada na lista
    return raizes

# Para resolver o problema para valores maiores que 10000pi
# Iremos assumir que todos esses valores convergem para
# pi/2, 3pi/2 e 5pi/2, respectivamente, o que e verdade

pi = math.pi

if Zm >= 10000*pi:
    raizes = [pi/2,3*pi/2,5*pi/2]
    for num in raizes:
            print("{:8.4f}".format(num))
else:
    if Zm > 5*math.pi/2:
        for num in funcao(xn,Zm):
            print("{:8.4f}".format(num))  # exibe raizes com 4 casas decimais
    else:
        print('Tente apenas Zm > 7.854')  # avisa que o Zm informado esta errado
     