# Neste EP, resolveremos integrais numericamente por meio da regra dos trapezios utilizando a funcao np.trapz

import numpy as np

Ndata = int(input())
xdata = np.zeros(Ndata)
ydata = np.zeros(Ndata)
for ii in range(Ndata):
    xdata[ii] = float(input())
    ydata[ii] = float(input())
a = xdata[0]
b = xdata[Ndata - 1]

# vamos converter tudo em np.array para fazermos as operacoes entre os valores das listas

u = (2*xdata - (a + b))/(b - a) # conversão dos coeficientes de x devido aos intervalos a e b
u = np.array(u)

P0 = 1  # P0 eh 1 para qualquer valor de u
def P1(u):  # define o polinomio P_1(u)
    return u
def P2(u):  # define o polinomio P_2(u)
    return u**2 - (1.0/3.0)
def P3(u):  # define o polinomio P_3(u)
    return u**3 - (3.0/5.0)*u
def P4(u):  # define o polinomio P_4(u)
    return u**4 - (6.0/7.0)*(u**2) + (3.0/35.0)
    
# agora, iremos definir os vetores vPj com j = 0,1,2,3,4 da mesma forma vista em aula
# como todas as funcoes sao arrays, converteremos vP0 em array tambem

vP0 = np.zeros(Ndata)
for i in range(Ndata):
    vP0[i] = P0
    
vP1 = P1(u)
vP2 = P2(u)
vP3 = P3(u)
vP4 = P4(u)

# encontraremos agora os valores de Aj com j = 0,1,2,3,4
# lembrando que Aj = integral de a ate b de (vPj)**2

A0 = np.trapz((vP0)**2,x = xdata)
A1 = np.trapz((vP1)**2,x = xdata)
A2 = np.trapz((vP2)**2,x = xdata)
A3 = np.trapz((vP3)**2,x = xdata)
A4 = np.trapz((vP4)**2,x = xdata)

# tendo os Aj, podemos encontrar os valores de valpha
# lembrando que valpha[j] = (1/Aj)*(integral de a ate b de ydata*(vPj))

valpha = [0,0,0,0,0]
valpha[0] = np.trapz(ydata*(vP0),x = xdata)/(A0)
valpha[1] = np.trapz(ydata*(vP1),x = xdata)/(A1)
valpha[2] = np.trapz(ydata*(vP2),x = xdata)/(A2)
valpha[3] = np.trapz(ydata*(vP3),x = xdata)/(A3)
valpha[4] = np.trapz(ydata*(vP4),x = xdata)/(A4)

# em seguida, podemos encontrar vphi
# lembrando que vphi[k] = soma de m=0 ate m=4 de valpha[m]*Pm(u[k])

vphi = np.zeros(Ndata)
for k in range(Ndata):  # encontra os valores de vphi para cada xdata fornecido
    vphi[k] = valpha[0]*P0 + valpha[1]*P1(u[k]) + valpha[2]*P2(u[k]) + valpha[3]*P3(u[k]) + valpha[4]*P4(u[k])

for ii in range(5) :
    print("{:10.6e}".format(valpha[ii]))
for ii in range(Ndata) :
    print("{:10.6e}".format(vphi[ii]))