# Aula 01: Manipulação Avançada de Dados com Pandas

## Explicação Conceitual
- Revisão dos principais conceitos do Pandas: DataFrame, Series, indexação e seleção de dados.
- Técnicas avançadas: filtragem condicional, uso de funções lambda, métodos de agregação e transformação.
- Operações de merge, join e concatenação para combinar diferentes conjuntos de dados.
- Tratamento de dados ausentes e inconsistentes: métodos fillna, dropna, replace.

## Prática com Exemplos
```python
import pandas as pd
# Exemplo de filtragem condicional
clientes = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [28, 35, 42],
    'cidade': ['SP', 'RJ', 'SP']
})
clientes_sp = clientes[clientes['cidade'] == 'SP']
print(clientes_sp)

# Exemplo de agrupamento
vendas = pd.DataFrame({
    'produto': ['A', 'B', 'A', 'C'],
    'valor': [100, 200, 150, 300]
})
vendas_agrupadas = vendas.groupby('produto').sum()
print(vendas_agrupadas)
```

## Exercícios
1. Carregue um DataFrame a partir de um arquivo CSV fictício e realize operações de filtragem e agrupamento.
2. Combine dois DataFrames usando merge e concatenação.
3. Identifique e trate valores ausentes em um DataFrame.

## Resolução dos Exercícios
```python
# 1. Carregar e filtrar
import pandas as pd
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [28, 35, 42, 30],
    'cidade': ['SP', 'RJ', 'SP', 'MG']
})
print(df[df['idade'] > 30])

# 2. Merge e concatenação
clientes = pd.DataFrame({'id': [1,2], 'nome': ['Ana', 'Bruno']})
pedidos = pd.DataFrame({'id': [1,2], 'produto': ['A', 'B']})
merged = pd.merge(clientes, pedidos, on='id')
print(merged)

# 3. Tratamento de valores ausentes
dados = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
dados_filled = dados.fillna(0)
print(dados_filled)
```
