# Aula 03 — Estatística Descritiva e Exploratória

## Objetivos
- Aplicar estatísticas descritivas para análise de dados.
- Compreender correlação entre variáveis.

## Explicação Conceitual
A estatística descritiva resume e interpreta dados. A análise exploratória identifica padrões, tendências e relações.

### Estatísticas Básicas
- Média, mediana, moda, desvio padrão
- Quartis, valores máximos e mínimos

### Correlação
- Relação entre variáveis
- Coeficiente de correlação de Pearson

## Prática com Exemplos
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [4, 3, 2, 1]})

# Estatísticas básicas
df.describe()

# Correlação
df.corr()
```

## Exercícios
1. Calcule a mediana e o desvio padrão de uma coluna numérica.
2. Analise a correlação entre duas colunas de um DataFrame.

## Resolução dos Exercícios
```python
# Exercício 1
df['a'].median(), df['a'].std()

# Exercício 2
df[['a', 'b']].corr()
```
