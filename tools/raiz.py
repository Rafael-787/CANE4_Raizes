from sympy import *
from .bisseccao import bisseccao_func
from .newton import newton_func

def raiz_func(intervalo,formula):
    w = ''
    print("Iniciando calculo de raiz")
    print(f"intervalo: {intervalo}")
    print(f"formula: {formula}")
    try:
        xk,u,_ = bisseccao_func(intervalo,formula)
    except Exception:
        print('erro bissecção')
        w = ['error','Erro no método de bissecção, cálculo interrompido']
        return '','','',w
    
    print(f"Finalizado bissecção: {xk}")

    try:
        r,i,e = newton_func(xk,formula)
    except:
        print('erro newton')
        w = ['warning','Erro ao calcular por newton, prosseguindo pelo método da bissecção.']
        r, u, e = bisseccao_func(intervalo,formula,limite=900)
        return r,u,e,w
    print("Finalizado Newton")
    print(f'raiz: {r}  iteração:{i+u}  erro:{e}')
    return r, i+u, e, w


if __name__ == "__main__":
    intervalo = (-5,0)
    x = symbols('x')
    exp = x**3 - 9*x +3
    exp1 = 3*x**3

    raiz_func(intervalo,exp1)