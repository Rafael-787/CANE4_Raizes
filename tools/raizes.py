from sympy import *
from .raiz import raiz_func

def raizes_func(intervalos,exp):
    dic = {}
    dic["aviso"] = []
    for n,i in enumerate(intervalos):
        r,it,e,w = raiz_func(i,exp)
        dic[n+1] = {
                "raiz":format(r,'.6e'),
                #"intervalo":i,
                "interações":it,
                "erro":format(e,'.2e'),
                }
        if w != '':
            dic["aviso"] = w
        #print(f" raiz {n+1} ok")
    return dic

if __name__ == "__main__":
    from intervalo import intervalo

    x = symbols('x')
    exp1 = x**3 - 9*x +3
    _,intervalos = intervalo(exp1)
    dict = raizes_func(intervalos,exp1)
    print(dict)