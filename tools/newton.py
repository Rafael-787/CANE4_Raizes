from sympy import *

def newton_func(xk,exp,limite:int=900):
    x = symbols('x')
    f = lambdify(x,exp,'numpy')
    derivada = diff(exp,x)
    f_dif = lambdify(x,derivada,'numpy')
    #print(f'derivada {derivada}')
    e = 1
    xk_old = xk
    u = 0


    while u < limite and e >= 10e-9:
        xk = xk - f(xk)/f_dif(xk)
        e = abs((xk)-xk_old)/abs(xk)
        xk_old = xk
        u += 1
        
    #print(f'raiz: {xk}  iteração:{u}  erro:{e}')
    return xk,u,e

if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz,iterações,erro = newton_func(-5,exp1)
    print(f'raiz: {raiz}  iteração:{iterações}  erro:{erro}')