**Aluno**: Rafael Carvalho Ferreira
**RA**: SC3042171

## Descrição

A rotina I tem como objetivo obter a raiz de uma expressão. O desenvolvimento seguiu como premissa as instrução disponíveis no *moodle* e que podem ser lidas no [README](https://github.com/Rafael-787/CANE4_Raizes/blob/master/README.md) da aplicação.

## Desenvolvimento

Foi criado um limite superior para o cálculo, sendo que só será possível encontrar as raízes que estiverem dentro desse limite superior (definido na v1 como \[-100,100]). É gerado um vetor com 1000 pontos dentro desse limite, que será utilizado como valores de *X*. Em seguida é calculado um vetor com os valores de *Y* para cada *X* correspondente calculado através da expressão. Com isso são procurados pontos de inversão ($f(a) * f(b) < 0$) que serão utilizados como intervalos de entrada para o método da bissecção. Esse irá iterar 3 vezes e retornará um valor de x que será usado como ponto inicial para o método de newton, que irá iterar até obter o erro desejado.

## Código

Transcrição das funções do código que executam as partes supracitadas.
### Intervalo

```Python
def intervalo_func(exp):

    interval = (-100,100) # Intervalo maior
    x = symbols('x')# Define x como variável da expressão
    
    # Transformação de matemática simbólica para numérica
    f = lambdify(x,exp,'numpy')

    # Cria uma lista com 10000 x entre o intervalo maior
    x_values = np.linspace(interval[0], interval[1], 1000)

    # Calcula o valor de Y para cada x
    y_values = f(x_values)

    # Cria uma matriz numpy com os valores xy
    data = np.vstack((x_values,y_values))

    # Faz a multiplicação dos elementos
    produto = y_values[1:] * y_values[:-1]

    # Cria uma lista com tuplas dos intervalos das raízes
    intervalos = [(lambda i: (data[0,i],data[0,i+1]))(i) for i in np.where(produto < 0)[0]]

    #print(intervalos)
    return data,intervalos
```

### Bissecção

```Python
def bisseccao_func (intervalo,exp):

    x = symbols('x') # Define x como variável da expressão
    
    # Transformação de matemática simbólica para numérica
    f = lambdify(x,exp,'numpy')

	# Define a como intervalo inferior e b como intervalo superior
    a,b = intervalo
    
    i_old = b # Inicializa variável para x(k-1)
    u = 0 # Inicializa contador de iterações
    e = 1 # Inicializa variável de erro
    
  

    while u < 3 or e < 10e-9:
        i = (a+b)/2 # Encontra média entre intervalo
        c = f(i) # Valor da expressão na média
        if c * f(b) <0 : # Atualização dos batentes do intervalo
            a = i
        else:
            b = i

        e = abs((i)-i_old)/abs(i) # Cálculo do erro
        i_old = i # Armazena x atual para ser usado como x(k-1)
        u += 1 # Incremento do contador de iterações

    return i,u
```

### Newton

```Python
def newton_func(xk,exp):

    x = symbols('x') # Define x como variável da expressão
    
    # Transformação de matemática simbólica para numérica
    f = lambdify(x,exp,'numpy') 
    
    derivada = diff(exp,x) # Define a derivada da expressão
    
    # Transformação de matemática simbólica para numérica
    f_dif = lambdify(x,derivada,'numpy') 
    
    e = 1 # Inicializa variável de erro
    xk_old = xk # Inicializa variável para x(k-1)
    u = 0 # Inicializa contador de iterações

    while e >= 10e-9 or u >= 90:
        xk = xk - f(xk)/f_dif(xk) # Fórmula do método
        e = abs((xk)-xk_old)/abs(xk) # Cálculo do erro
        xk_old = xk # Armazena x atual para ser usado como x(k-1)
        u += 1 # Incremento do contador de iterações
        
    return xk,u,e
```

### Junção

```Python
def raiz_func(intervalo,formula)
	# Inicia a iteração por bissecção e armazena o valor de x (xk) e número de iterações (u) ao final.
    xk,u = bisseccao_func(intervalo,formula)
    
    # Inicia a iteração por Newton com xk como aproximação incial e armazena a raiz encontrada, o númerto de iterações e o erro ao final.
    r,i,e = newton_func(xk,formula)
    return r, i+u, e
```

## Uso

O código completo pode ser acessado através do [GitHub](https://github.com/Rafael-787/CANE4_Raizes.git) do projeto. Para uma interação mais orgânica, foi utilizada a biblioteca Streamlit para criação de uma UI. Isso também possibilitou que a aplicação fosse hospedada na nuvem comunitária *Streamlit Community Cloud* e pode ser acessado e utilizado de qualquer lugar através desse [link](https://cane4raizes.streamlit.app/). A imagem a seguir apresenta a página inicial com a área de entrada para a expressão e as duas ações disponíveis.

![[Pasted image 20240901003336.png]]

A expressão deve ser escrita seguindo a tabela de operadores a seguir:

| Operador | Função        | Exemplo  | Resultado        |
| -------- | ------------- | -------- | ---------------- |
| *        | multiplicação | x*2      | $2x$             |
| /        | divisão       | x/2      | $\frac{x}{2}$    |
| +        | soma          | x + 2    | $x + 2$          |
| -        | subtração     | x - 2    | $x - 2$          |
| **       | exponência    | x**(3/4) | $x^ \frac{3}{4}$ |
| sqrt()   | raiz quadrada | sqrt(x)  | $\sqrt{x}$       |
| cos()    | cosseno       | cos(x)   | $\cos{x}$        |
| sin()    | seno          | sin(x)   | $\sin{x}$        |
| tan()    | tangente      | tan(x)   | $\tan{x}$        |
| e        | euler         | e**x     | $e^x$            |
| pi       | pi            | pi*x     | $\pi x$          |

Após escrita, recomenda-se utilizar o opção "**Visualizar**" para poder ver a equação, simplificada, escrita em matemática simbólica e o seu gráfico, para conferir se corresponde ao digitado.

![[Pasted image 20240901003724.png]]

Verificada a expressão, clique em calcular para visualizar todas as raízes presentes dentro do intervalo \[-100,100].

![[Pasted image 20240901003925.png]]
