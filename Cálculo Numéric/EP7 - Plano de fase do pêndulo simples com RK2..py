import numpy as np;

m = float(input()); # em kg
l = float(input()); # em m
h = float(input()); # em s
Tf = float(input()); # em s
theta0 = float(input()); # em rad
p0 = float(input()); # em kg m^2/s
g = 10 # em m/s^2

Nt = np.size(np.arange(0.0,Tf+h,h)) # encontra o numero de passos

thetat = np.zeros(Nt)
pt = np.zeros(Nt)
thetat[0] = theta0 # define o 'theta' inicial (antes do primeiro passo)
pt[0] = p0 # define o 'p' inicial (antes do primeiro passo)

# Caso quisessemos criar uma lista que exibe os valores de energia:
# energia0 = (p0**2)/(2*m*l**2) + m*g*l*(1-np.cos(theta0))
# energia = np.zeros(Nt)
# energia[0] = energia0

# vamos criar uma estrutura com while para executar e armazenar cada passo pelo metodo RK2
i = 0
while i+1 < Nt:
    
    # primeiramente, definimos kp_1 e ktheta_1, de acordo com as EDOs
    kp_1 = -m*g*l*np.sin(thetat[i])
    ktheta_1 = pt[i]/(m*l**2)
    
    # posteriormente, encontramos o meio passo p_meio e theta_meio
    p_meio = pt[i] + kp_1*h/2
    theta_meio = thetat[i] + ktheta_1*h/2
    
    # em seguida, definimos kp_2 e ktheta_2, de forma analoga a kp_1 e ktheta_1
    kp_2 = -m*g*l*np.sin(theta_meio)
    ktheta_2 = p_meio/(m*l**2)

    # finalmente, podemos encontrar o proximo passo, ou seja, i+1
    pt[i+1] = pt[i] + kp_2*h
    thetat[i+1] = thetat[i] + ktheta_2*h
    
    # Caso quisessemos atualizar o valor da energia apos cada passo:
    # energia[i+1] = (pt[i+1]**2)/(2*m*l**2) + m*g*l*(1-np.cos(thetat[i+1]))

    # para que o angulo theta fique entre -pi e pi, podemos criar as seguintes condicoes:
    if thetat[i+1] >= np.pi:
        thetat[i+1] = thetat[i+1] - 2*np.pi
    elif thetat[i+1] <= - np.pi:
        thetat[i+1] = thetat[i+1] + 2*np.pi
    
    i = i + 1 # atualiza o passo para a proxima repeticao

# agora, basta printar os resultados de theta e de p
for ii in range(Nt) :
     print("{:10.6e}".format(thetat[ii]));
for ii in range(Nt) :
     print("{:10.6e}".format(pt[ii]));
     
# Caso quisessemos verificar se a energia se mantem constante:
# for ii in range(Nt) :
#     print("{:10.6e}".format(energia[ii]));
