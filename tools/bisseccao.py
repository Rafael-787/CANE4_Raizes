from sympy import *

def bisseccao_func (intervalo,exp,limite:int=3):
    x = symbols('x')
    a,b = intervalo
    i_old = b
    u = 0
    e = 1
    f = lambdify(x,exp,'numpy')

    while u < limite and e >= 10e-9:
        i = (a+b)/2
        c = f(i)
        if c * f(b) <0 : 
            a = i
        else:
            b = i

        #print(f"i:{i} i_old:{i_old}")
        e = abs((i)-i_old)/abs(i)
        i_old = i
        u += 1
        #print(u)

    #print(f"Raiz: {i}  iterações:{u}")
    return i,u,e

if __name__ == "__main__":
    
    intervalo = (-4.1703170317031635, -3.1503150315031405)
    x = symbols('x')
    exp1 = x**3 - 9*x +3

    raiz, iterações = bisseccao_func(intervalo,exp1)
    print(f"Raiz: {raiz}  iterações:{iterações}")