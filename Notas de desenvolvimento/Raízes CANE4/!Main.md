Página principal do desenvolvimento da rotina.
# Sumário
- [Instruções](#Instruções)
- [Pontuação](#Pontuação)
- [Funções Teste](#Funções_teste)
- [Outras Páginas](#Outras_Páginas)
## Instruções

1. Construir o [gráfico](Gráfico) da função
    
2. Identificar um [intervalo](Intervalo) que contém a raiz
    
3. [Verificar](Verificação) algebricamente que existe raiz no intervalo indicado
    
4. Faça três iterações do método da [**_bissecção_**](https://moodle.scl.ifsp.edu.br/pluginfile.php/296519/mod_resource/content/2/2_Me%CC%81todo%20da%20bissecc%CC%A7a%CC%83o.pdf) a partir de um intervalo dado (x0, x1 e x2);
    
5. Resolva a raiz da equação pelo método de [**_Newton_**](https://moodle.scl.ifsp.edu.br/pluginfile.php/296525/mod_resource/content/1/4_Me%CC%81todo%20de%20Newton.pdf) usando x2 obtido em (1) como aproximação inicial e erro E=10-9.
    
6. Dados de saída:
    - raiz encontrada;
    - número de iterações;
    - erro.

## Pontuação:

- [x] Construção do gráfico ***(1.0)***

- [x] O intervalo é identificado pela rotina ***(1.0)*** 
	- Intervalo das raízes encontradas no intervalo maior de \[-100,100]

- [x] Verificação algébrica ***(1.0)***
	- Embutida dentro do encontro do intervalo

- [x] Uso do método da bissecção corretamente ***(2.5)***

- [x] Derivada é resolvida pela rotina ***(1.0)***

- [x] Uso do método de Newton corretamente (2.5)

- [x] Dados de saída (1.0)

## Funções teste

 - $f(x) = x^3 - 1$
	 - ` x**3 -1 `
 - $f(x) = x^3 -9x +3$
	 - ` x**3 -9*x +3 `
 - $f(x) = e^x -2x -1$
	 - ` e**x -2*x -1 `
 - $f(x) = cos\frac{\pi*(x+1)}{8}+0.148x-0.9062$
	 - ` cos((pi*(x+1))/8) + 0.148*x - 0.9062`
	 - \[-1,10] -> 3 raízes

## Outras Páginas
- [Gráfico](Gráfico)
- [Intervalo](Intervalo)
- [Verificação algébrica](Verificação)
- [Questões técnicas](Técnico)

