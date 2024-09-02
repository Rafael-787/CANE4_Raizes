import time
import sympy as sp

x = sp.symbols('x')

eq = sp.cos((sp.pi*(x+1))/8) + 0.148*x - 0.9062

lista = range(1,11)

n = 0
i = 1
print("Início iteração simbólica \n")
start_geral = time.perf_counter()
while n < 10:
    start_it = time.perf_counter()
    res = eq.subs(x,i)
    dif_time = time.perf_counter() - start_it
    #print(res)
    i = res
    n += 1
    print(f"Iteração nº {n} levou {dif_time}s")

diff_geral = time.perf_counter() - start_geral
print("")
print("Resultado geral simbólico")
print("---------------------------")
print(f"Número de iterações: {n}")
print(f"Tempo total: {diff_geral}s \n")

print("---------------------------")
print("Início iteração numérica")
n = 0
i = 1
start_geral = time.perf_counter()
while n < 10:
    start_it = time.perf_counter()
    res = eq.subs(x,i).evalf()
    dif_time = time.perf_counter() - start_it
    #print(res)
    i = res
    n += 1
    print(f"Iteração nº {n} levou {dif_time}s")

diff_geral = time.perf_counter() - start_geral
print("")
print("Resultado geral numérico")
print("---------------------------")
print(f"Número de iterações: {n}")
print(f"Tempo total: {diff_geral}s")