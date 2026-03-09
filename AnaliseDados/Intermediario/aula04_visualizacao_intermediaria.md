# Aula 04 — Visualização Intermediária

## Objetivos
- Criar gráficos para análise visual de dados.

## Explicação Conceitual
Visualizações facilitam a compreensão de padrões e tendências. Gráficos como dispersão, histogramas e boxplots são essenciais para análise exploratória.

### Tipos de Gráficos
- Dispersão (scatter)
- Histograma
- Boxplot

## Prática com Exemplos
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'x': [1,2,3,4], 'y': [10,20,25,30]})

# Gráfico de dispersão
df.plot.scatter(x='x', y='y')
plt.show()

# Histograma
df['y'].plot.hist()
plt.show()

# Boxplot
df['y'].plot.box()
plt.show()
```

## Exercícios
1. Crie um histograma para uma coluna numérica de um DataFrame.
2. Gere um boxplot para comparar duas colunas.

## Resolução dos Exercícios
```python
# Exercício 1
df['x'].plot.hist()
plt.show()

# Exercício 2
df[['x', 'y']].plot.box()
plt.show()
```
