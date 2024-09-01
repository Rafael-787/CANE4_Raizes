Área dedicada a condições técnicas da execução do programa.

## Sumário

- [*Imports* padrões](#Imports_padrões)
- [*Requirements*](#Requirements)
- [Complicações](#Complicações)
- [Definições](#Definições)
- [UX](#UX)

## *Imports* padrões

``` python
from sympy import *
from sympy import Poly
import matplotlib.pyplot as plt
import numpy as np
```

``` CMD
streamlit run e:\Documentos\#Arquivos em geral\[00] EAR\Calc. Numerico\Raizes\main.py
```

## Requirements

``` Python
SymPy
matplotlib
```

## Definições
- Limitantes por arquivo de configuração.
- Limite de iterações definido em config.
	- Limite bissecção
	- Limite Newton
- Erro definido em config

## Complicações

- [x] Como será o input das fórmulas?
	 - Transformar *string* em fórmula sympy?

- A criação de pontos diminuiu para 1000, em teste percebeu-se que 10000 criava um intervalo muito próximo da raiz criando um loop infinito na bissecção.


## *UX*

- Será usado o Streamlit para que o código possa ser feito o *deploy* no [StreamlitApps](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
- 2 páginas
	- Cálculo
	- Configurações

## Tools
- Uma função para calcular a parte por bissecção, limitada internamente a 3 iterações.
		- Input - Fórmula, intervalo
		- Output - raiz, nº iterações
- Função cálculo por newton, limitada pelo erro ou nº máximo de iterações.
	- Input - Fórmula, aproximação inicial (xk)
	- Output - raiz, nº iterações, erro
- Função raízes
	- Input - Intervalo, fórmula
	- Output - Raiz, Interações, erro
- Função intervalo
	- Cria uma matriz numpy com os valores xy e os intervalos de inversão
	- Input - fórmula
	- output - data, intervalos
