
- Gerado no [intervalo](obsidian://open?vault=Obsidian&file=Ra%C3%ADzes%20CANE4%2FIntervalo) \[-100,100] com 1000 pontos
	- Em testes 10000 pontos criou um intervalo muito próximo da raiz criando um loop infinito.
- Opção de manter escala ativada nas configurações (ver tabela)

| Estado | Resposta                                                                                                                     |
| ------ | ---------------------------------------------------------------------------------------------------------------------------- |
| True   | Escala em y limitada no intervalo de x. Gráfico mantém as características visuais mas reduz quantidade de pontos de análise. |
| False  | Mantém todos os valores de y. Gráfico pode ter distorções visuais porém mantém todos os pontos calculados de y.              |
- Dar a opção de mostrar um zoom no intervalo das raízes
	- Gerar um gráfico geral e *snaps* para cada raiz

### Plot 


``` Python

x_values = np.linspace(intervalo[0], intervalo[1], 10000)
y_values = f(x_values)
plt.plot(x_values,y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.ylim(intervalo[0],intervalo[1]) #condição nas configurações
#plt.axvline(x=i, color='blue', linestyle='--', label=f'Raiz {round(i,3)}')
#plt.legend()
plt.grid(True)
plt.show()
```
