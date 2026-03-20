# Aula 05: Visualização Básica de Dados

## Objetivos
- Criar gráficos simples com pandas e matplotlib.

## Explicação Conceitual
Visualização ajuda a entender padrões e tendências. Funções: `plot`, `hist`, `bar`.

## Prática com Exemplos
```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})
df['X'].plot()
plt.show()
df['Y'].plot(kind='bar')
plt.show()
df['X'].plot(kind='hist')
plt.show()
```

## Exercícios
1. Plote um gráfico de barras para a coluna 'Y'.
2. Plote um histograma para a coluna 'X'.

## Resolução dos Exercícios
1.
```python
df['Y'].plot(kind='bar')
plt.show()
```
2.
```python
df['X'].plot(kind='hist')
plt.show()
```