# Aula 01 — Limpeza e Preparação de Dados

## Objetivos
- Compreender a importância da limpeza de dados.
- Aprender técnicas para tratar valores ausentes e converter tipos de dados.

## Explicação Conceitual
A limpeza de dados é uma etapa fundamental na análise, pois dados brutos geralmente contêm inconsistências, valores ausentes e tipos inadequados. Garantir dados limpos é essencial para análises confiáveis.

### Valores Ausentes
- Identificação de valores nulos (NaN, None)
- Estratégias: remoção, substituição por média/mediana/moda, interpolação

### Conversão de Tipos
- Conversão de strings para datas, números, categorias
- Detecção de tipos inadequados

## Prática com Exemplos
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', None],
    'idade': [23, np.nan, 35, 29],
    'data_nascimento': ['2000-01-01', '1998-05-12', None, '1997-07-30']
})

# Identificar valores ausentes
df.isnull()

# Remover linhas com valores ausentes
df.dropna()

# Preencher valores ausentes
df['idade'].fillna(df['idade'].mean(), inplace=True)

# Converter coluna para data
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
```

## Exercícios
1. Carregue um DataFrame com valores ausentes e aplique diferentes estratégias de tratamento.
2. Converta colunas de tipos inadequados para os tipos corretos.

## Resolução dos Exercícios
```python
# Exercício 1
# ...carregar DataFrame...
df.fillna(0)  # Exemplo de preenchimento

# Exercício 2
df['coluna'] = df['coluna'].astype(int)
```
