~~Definitivamente a parte mais difícil desse código~~

O código dever ser capaz de encontrar de forma autônoma o intervalo das raízes.

- Colocar uma opção para o operador inserir o intervalo ou para ser encontrado automaticamente. (Não implementado)
### Comparativo entre modelos

| [**Atual**](#Atual)                                                                                | [**Desejado**](#Desejado)                                                                                                              |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| São gerados ***1000*** pontos no intervalo **\[-100,100]** e é procurada a inversão nesses pontos. | Não há um intervalo maior onde será feita a pesquisa, as áreas de inversão são detectadas por cálculo antes da definição do intervalo. |

### Atual
| Fraqueza                                            | Vantagem                 |
| --------------------------------------------------- | ------------------------ |
| Não cobre raízes fora do intervalo pré-determinado. | Simplicidade de solução. |
- Fazer a multiplicação dos elementos da matriz solução dentro do intervalo \[-100,100] e identificar as inversões pela lógica $f(a) * f(b) <0$.

```Python
y_values = f(x_values)

produto = y_values[1:] * y_values[:-1]

print(produto)

np.where(produto < 0)
```

- A *array* produto retorna o produto dos intervalos com tamanho igual ``len(y_values) - 1``.
- O comando ``np.where(produto < 0)`` retorna o índice dos produtos que identificam uma inversão na *array* produto. Os valores de $a$ e $b$ do intervalo são encontrados como mostrado abaixo:
	- $a$ = índice ``np.where(produto < 0)
	- $b$ = índice ``np.where(produto < 0)`` + 1
		- O acréscimo de 1 em b se deve a diferença de tamanho entre as *arrays*, a multiplicação é feita com o valor do índice atual pelo valor do índice posterior.

``` Python
# Faz a multiplicação dos elementos
produto = y_values[1:] * y_values[:-1]

# Cria uma lista com tuplas dos intervalos das raízes
intervalos = [(lambda i: (i,i+1))(i) for i in np.where(produto < 0)[0]]
```

#### Fora do range

- $f(x) = (x−200)^2−25$
	- raízes (195, 205)

### Desejado
| Fraqueza                                                                              | Vantagem                                        |
| ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Dificuldade de implementação e necessidade de pré-cálculos, possivelmente mais lento. | Cobre raízes fora do intervalo pré-determinado. |

#### Táticas para implementação

- Encontrar pontos críticos pela derivada = 0
	- E no caso de função que não podem ser derivadas?
	- Funções sem raízes reais
	- Raízes sem ponto crítico
		- Retas
	- $f(x) = cos\frac{\pi*(x+1)}{8}+0.148x-0.9062$
		- Vários momentos com dx = 0
		
		 ![[Função 4.png]]
		 
- A partir do ponto crítico verificar inversão para encontrar *range*
	- X³ que só possui uma após o crítico
	- Verificar se derivada crescente ou decrescente para ver onde procurar (esquerda ou direita)
		- Encontrar onde dx = 0 e substituir em f(x)
			- if f(dx) < 0 
				- Verificar onde dx crescente (esquerda ou direita)
			- If f(dx) >0
				- verificar onde dx decrescente (esquerda ou direita)
	- Fazer iteração de um range de x casas entre ponto crítico para verificar mudança de sinal
		- É possível usar dx para definir um *range* x mais preciso?
	- Múltiplos pontos críticos
		- Verificar de alguma forma através da derivada se faz sentido continuar verificando outros pontos críticos.
		- Função se assemelha a uma reta....