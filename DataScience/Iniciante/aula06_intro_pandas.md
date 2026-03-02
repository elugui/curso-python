# Aula 06 — Introdução ao Pandas

## Explicação Conceitual
- O que é o Pandas? Estruturas Series e DataFrame.
- Diferença entre Series e DataFrame.
- Leitura de arquivos (CSV, Excel).
- Manipulação básica de dados.

## Prática com Exemplos
```python
import pandas as pd

# Criando uma Series
s = pd.Series([10, 20, 30])
print(s)

# Criando um DataFrame
df = pd.DataFrame({"nome": ["Ana", "Bruno"], "idade": [25, 30]})
print(df)

# Lendo um arquivo CSV
# df = pd.read_csv("dados.csv")
```

## Exercícios
1. Crie uma Series com 4 valores numéricos.
2. Crie um DataFrame com nomes e idades de 3 pessoas.
3. Explique a diferença entre Series e DataFrame.

## Resolução dos Exercícios
```python
import pandas as pd
# Exercício 1
s = pd.Series([1, 2, 3, 4])

# Exercício 2
df = pd.DataFrame({"nome": ["Carlos", "Diana", "Eduardo"], "idade": [22, 28, 35]})

# Exercício 3
# Series é unidimensional, DataFrame é bidimensional (tabela).
```
