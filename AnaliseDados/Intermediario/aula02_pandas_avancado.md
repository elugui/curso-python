# Aula 02 — Manipulação Avançada com pandas

## Objetivos
- Aprender a agrupar, agregar e combinar DataFrames.

## Explicação Conceitual
O pandas permite manipulações avançadas de dados, como agrupamentos, agregações e junções, essenciais para análises complexas.

### Agrupamento (groupby)
- Agrupar dados por uma ou mais colunas
- Aplicar funções de agregação (soma, média, contagem)

### Mesclagem e Concatenação
- Mesclar DataFrames (merge, join)
- Concatenar DataFrames (concat)

## Prática com Exemplos
```python
import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'A', 'B', 'B'],
    'valor': [10, 15, 10, 20]
})

# Agrupar e somar
df.groupby('categoria').sum()

# Concatenar DataFrames
pd.concat([df, df])

# Mesclar DataFrames
df2 = pd.DataFrame({'categoria': ['A', 'B'], 'desc': ['foo', 'bar']})
pd.merge(df, df2, on='categoria')
```

## Exercícios
1. Agrupe um DataFrame por uma coluna e calcule a média dos valores.
2. Mescle dois DataFrames com base em uma coluna comum.

## Resolução dos Exercícios
```python
# Exercício 1
df.groupby('categoria')['valor'].mean()

# Exercício 2
pd.merge(df, df2, on='categoria')
```
