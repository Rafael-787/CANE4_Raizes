import numpy as np

def escalonamento(ma,mb):
    u = np.hstack((ma,mb))

    n_trocas = 0
    ordem, colunas = u.shape # Ordem da matrix

    #Considera que a matrix é quadrada, verificar se é possível matrix não quadrada
    for j in range(colunas-1): #Itera entre as colunas menos a final
        #print(f"coluna {j}: {u[j:,j]}")
        id_pivo = np.argmax(u[j:,j])+j
        #print(f"id_pivo coluna {j}: {id_pivo}")
        if id_pivo == j:
            pivo = u[j,id_pivo]
            #print(f"Pivo correto: {pivo}")
            #print(u)


        else:
            #print(f"Trocando linhas {j} e {id_pivo} ")
            #print('U antigo')
            #print(u)
            u[[j,id_pivo]] = u[[id_pivo,j]]
            #print('u novo')
            #print(u)
            n_trocas += 1
            #print(f" Troca nº: {n_trocas}")
            pivo = u[j,j]
            #print(f"Pivo: {pivo}")
        for i in range(j+1,ordem): #Não itera a 1º linha
            m = u[i,j]/pivo
            #print(f"m = {u[i,j]}/{pivo} = {m}")
            u[i,:] = u[i,:] - m*u[j,:]
            #print(f"L{i+1} = L{i+1} - {m}*L{j+1}")
            #print(u)
        
        #print("-----------------------------------------")

    #print(f"Ordem: {ordem}")
    #print(f"Nº trocas: {n_trocas}")
    #print(u)
    return u,ordem,n_trocas

def res_sistema(u):
    # Resolução do sistema
    res = []

    for n,i in enumerate(u[::-1]):
        #print(f"X{len(u)-n}")
        #print()
        #print(f"linha: {i}")
        #print(f"valor igualdade: {round(i[-1],3)}")
        #print(f"coeficientes: {i[-(n+1):-1]}")

        subtracao = 0
        for k,a in enumerate(i[-(n+1):-1]):
            #print(f"c inicial: {subtracao}")
            #print(f"res: {res}")
            #print(f"calculo: {a} * {res[k-1]}")
            subtracao += a*res[k-1]
            #print(f"c final: {subtracao}")
            #print()

        x = (i[-1]-subtracao)/i[-(n+2)]
        #print()
        #print(f"X{len(u)-n} = {round(i[-1],3)} - {round(subtracao,3)} / {round(i[-(n+2)],3)}")
        subtracao = 0
        res.append(round(x,3))
        #print(f"X{len(u)-n} = {round(x,3)}")
        #print("----------------------------")
        #print()

    res = res[::-1]
    #print(f"Resolução: {res}")
    return res   

def met_gauss(ma,mb):
    dic = {}
    # Cálculo da determinante
    det = np.linalg.det(ma)
    if det == 0:
        dic["aviso"]  = "Sistema indeterminado"
        return dic
    
    else:
        escalonada,ordem,n_trocas = escalonamento(ma,mb)
        res = res_sistema(escalonada)

        dic ={
            "resolução":res,
            "ordem":ordem,
            "n_trocas":n_trocas,
            "escalonada":escalonada,
            "aviso":""
        }

        return dic

if __name__ == "__main__":
    # Área para testes
    ma = np.array([[8,1,1],[1,5,1],[2,1,2]],dtype=float)
    mb = np.array([[20],[10],[11]],dtype=float)
    print(met_gauss(ma,mb))