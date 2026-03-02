# Aula 05: Pré-processamento de Dados para ML

## Explicação Conceitual
- Importância do pré-processamento para a qualidade dos modelos.
- Normalização e padronização de dados.
- Codificação de variáveis categóricas: one-hot, label encoding.
- Seleção e extração de features.
- Divisão de dados em treino e teste.

## Prática com Exemplos
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Normalização e padronização
df = pd.DataFrame({'idade': [20, 30, 40], 'salario': [2000, 3000, 4000]})
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
print(df_scaled)

# Codificação categórica
cidades = pd.DataFrame({'cidade': ['SP', 'RJ', 'MG']})
ohe = OneHotEncoder(sparse=False)
cidades_encoded = ohe.fit_transform(cidades)
print(cidades_encoded)

# Divisão treino/teste
X = df
y = [0, 1, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train, X_test)
```

## Exercícios
1. Normalize um conjunto de dados numéricos.
2. Aplique one-hot encoding em uma coluna categórica.
3. Divida um DataFrame em conjuntos de treino e teste.

## Resolução dos Exercícios
```python
# 1. Normalização
from sklearn.preprocessing import MinMaxScaler
dados = pd.DataFrame({'nota': [2, 5, 8, 10]})
scaler = MinMaxScaler()
print(scaler.fit_transform(dados))

# 2. One-hot encoding
cidades = pd.DataFrame({'cidade': ['SP', 'RJ', 'MG', 'SP']})
ohe = OneHotEncoder(sparse=False)
print(ohe.fit_transform(cidades))

# 3. Split treino/teste
X = dados
y = [0, 1, 1, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
print(X_train, X_test)
```
