# Aula 03: Leitura e Escrita de Arquivos

## Objetivos
- Ler e salvar dados em arquivos CSV, Excel e JSON.

## Explicação Conceitual
O pandas permite importar e exportar dados facilmente. Funções: `read_csv`, `read_excel`, `to_csv`, `to_excel`.

## Prática com Exemplos
```python
import pandas as pd
# Leitura de CSV
df = pd.read_csv('dados.csv')
print(df.head())
# Salvando em Excel
df.to_excel('saida.xlsx')
```

## Exercícios
1. Leia um arquivo CSV fictício e mostre as 5 primeiras linhas.
2. Salve um DataFrame criado em aula em um arquivo JSON.

## Resolução dos Exercícios
1.
```python
df = pd.read_csv('exemplo.csv')
print(df.head())
```
2.
```python
df.to_json('saida.json')
```