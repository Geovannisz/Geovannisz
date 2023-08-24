import numpy as np

Np=int(input())
TD=float(input())
Ntemp=int(input())
vTemp=np.zeros(Ntemp)
for ii in range(Ntemp):
     vTemp[ii]=float(input())

e = 2.718281828459045235360287  # numero de euler com precisao maior do que a necessaria
uk,w_u = np.polynomial.legendre.leggauss(Np)  # raizes e pesos do polinomio de legendre no intervalo [-1,1]

cv = []  # lista que colocaremos os valores obtidos de C_v(vTemp)/k_B

# como C_v varia em funcao de vTemp, iremos criar uma repeticao para calcular o valor de C_v para cada vTemp

for i in range(Ntemp):
    T = vTemp[i]  # atribui um novo valor de vTemp a T
    a = 0         # limite inferior da integral
    b = TD/T      # limite superior da integral
    
    # aplicaremos a transformacao das raizes e dos pesos do intervalo [-1,1] para o intervalo [a,b]
    
    xk = (1/2)*((b - a)*uk + (a + b))
    w_x = (b - a)*(w_u/2)
    
    # definiremos agora f(x_k)
    
    fx = ((xk**4)*e**xk)/((e**xk - 1)**2)

    # a aproximacao da integral pela quadratura de Gauss-Legendre eh dada pela somatoria de k = 1 ate Np do produto dos pesos com os f(x_k)

    integral = sum(w_x*fx)
    
    cvTemp = 9*(1/b)**3*integral  # valor de C_v(vTemp = T)/K_B
    cv.append(cvTemp)             # lista que armazena os valores obtidos de C_v/K_B a cada repeticao

for ii in range(Ntemp) :
     print("{:10.6e}".format(cv[ii]))