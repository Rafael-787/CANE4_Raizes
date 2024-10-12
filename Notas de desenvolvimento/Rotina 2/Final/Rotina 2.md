**Aluno**: Rafael Carvalho Ferreira
**RA**: SC3042171

## Descrição

A rotina II tem como objetivo obter a resolução de um sistema linear possível e determinado através do método de eliminação de Gauss
## Código

Transcrição das funções do código que executam as partes supracitadas.
### Escalonamento

```Python
def escalonamento(ma,mb):

    u = np.hstack((ma,mb))
    n_trocas = 0
    ordem, colunas = u.shape # Ordem da matrix


    for j in range(colunas-1): #Itera entre as colunas menos a final
        id_pivo = np.argmax(u[j:,j])+j #Encontra a posição do maior valor na coluna

        if id_pivo == j: #Verifica se o pivô da linha é o maior valor
            pivo = u[j,id_pivo] #Defini o pivô
  
        else: #Caso não seja
            u[[j,id_pivo]] = u[[id_pivo,j]] #Efetua troca de linhas
            n_trocas += 1 #Aumenta contador de trocas
            pivo = u[j,j] #Define o pivô após troca

        for i in range(j+1,ordem): #Itera entre as linhas menos a primeira
            m = u[i,j]/pivo #Calcula o m para a linha
            u[i,:] = u[i,:] - m*u[j,:] #Atualiza o valor da linha escalonada

    return u,ordem,n_trocas
```

### Resolução do sistema

```Python
def res_sistema(u):

    res = [] #Inicializa variável que receberá o resultado
  
    for n,i in enumerate(u[::-1]): #Itera entre as linhas, de baixo para cima
        subtracao = 0 #Inicializa de subtração
        #Essa variável é responsável por subtrair o valor do resultado (mb) pelos valores dos 'Xn' já calculados pelos seus coeficientes.

        for k,a in enumerate(i[-(n+1):-1]): #Itera pelos coeficientes dos Xn já calculados
            subtracao += a*res[k-1] #Xn * coeficiente

        x = (i[-1]-subtracao)/i[-(n+2)] #mbn - subtração / xn
        subtracao = 0 #zera a variável para a próxima linha
        res.append(round(x,3)) #Acrescenta o valor de Xn na variável de resultados

    res = res[::-1] #Inverte ordem dos valores para seguir ordem crescente (X1, X2,...)
    
    return res
```

### Método de gauss

```Python
def met_gauss(ma,mb):

    dic = {} #Inicializa dicionário de resposta

    det = np.linalg.det(ma) #Calcula a determinante de ma

    if det == 0: #Verifica se o sistema é PI
        dic["aviso"]  = "Sistema indeterminado" #Salva apenas aviso de SI
        return dic

    else: #Caso não seja PI
        escalonada,ordem,n_trocas = escalonamento(ma,mb) #Execução função escalonamento
        res = res_sistema(escalonada) #Executa a função de resolução do sistema com a matrix escalonada
        dic ={ #Salva os valores obtidos no dicionário de resposta
            "resolução":res,
            "ordem":ordem,
            "n_trocas":n_trocas,
            "escalonada":escalonada,
            "aviso":""
        }

  
        return dic
```

## Uso

O código completo pode ser acessado através do [GitHub](https://github.com/Rafael-787/CANE4_Raizes.git) do projeto. Para uma interação mais orgânica, foi utilizada a biblioteca Streamlit para criação de uma UI. Isso também possibilitou que a aplicação fosse hospedada na nuvem comunitária *Streamlit Community Cloud* e pode ser acessado e utilizado de qualquer lugar através desse [link](https://cane4raizes.streamlit.app/). A imagem a seguir apresenta a página inicial com a área de entrada para a as matrizes e como é apresentado os resultados.


![[Pasted image 20241012142508.png]]

Na área detalhes é possível ter acesso à ordem do sistema, número de trocas efetuadas pela pivotação e a matrix escalonada.

![[Pasted image 20241012142708.png]]
