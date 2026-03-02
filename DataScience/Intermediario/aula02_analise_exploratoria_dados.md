# Aula 02: Análise Exploratória de Dados (EDA)

## Explicação Conceitual
- O que é EDA: processo de investigação inicial dos dados para descobrir padrões, detectar anomalias e testar hipóteses.
- Estatísticas descritivas: média, mediana, moda, desvio padrão, quartis.
- Visualização de dados: histogramas, boxplots, scatter plots.
- Identificação de outliers e padrões.

## Prática com Exemplos
```python
import pandas as pd
import matplotlib.pyplot as plt
# Exemplo de estatísticas descritivas
df = pd.DataFrame({'idade': [22, 35, 58, 41, 29, 33, 40]})
print(df.describe())

# Exemplo de histograma
df['idade'].hist()
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Exemplo de boxplot
plt.boxplot(df['idade'])
plt.ylabel('Idade')
plt.show()
```

## Exercícios
1. Calcule as principais estatísticas descritivas de um DataFrame.
2. Crie um histograma e um boxplot para uma coluna numérica.
3. Identifique possíveis outliers em um conjunto de dados.

## Resolução dos Exercícios
```python
# 1. Estatísticas descritivas
df = pd.DataFrame({'salario': [2000, 2500, 3000, 4000, 10000]})
print(df.describe())

# 2. Visualizações
import matplotlib.pyplot as plt
df['salario'].hist()
plt.show()
plt.boxplot(df['salario'])
plt.show()

# 3. Outliers
q1 = df['salario'].quantile(0.25)
q3 = df['salario'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['salario'] < q1 - 1.5*iqr) | (df['salario'] > q3 + 1.5*iqr)]
print(outliers)
```
