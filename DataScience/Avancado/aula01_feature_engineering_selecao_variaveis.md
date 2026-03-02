# Aula 01: Feature Engineering e Seleção de Variáveis

## Explicação Conceitual
- O que é feature engineering: criação, transformação e seleção de variáveis para melhorar modelos.
- Técnicas: encoding, binning, extração de data/hora, interação de variáveis.
- Seleção de variáveis: métodos filter, wrapper e embedded.
- Importância de features: análise de importância, eliminação de variáveis irrelevantes.

## Prática com Exemplos
```python
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectFromModel

# Carregar dados
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target

# Feature importance com Random Forest
rf = RandomForestRegressor().fit(df, y)
importancias = rf.feature_importances_
print('Importância das features:', importancias)

# Seleção automática de variáveis
selector = SelectFromModel(rf, prefit=True)
X_selected = selector.transform(df)
print('Shape após seleção:', X_selected.shape)
```

## Exercícios
1. Crie novas features a partir de um dataset (ex: interação, binning).
2. Utilize um modelo para identificar as variáveis mais importantes.
3. Elimine variáveis irrelevantes e avalie o impacto no modelo.

## Resolução dos Exercícios
```python
# 1. Interação de features
df['CRIM_X_RM'] = df['CRIM'] * df['RM']

# 2. Importância das variáveis
importancias = rf.feature_importances_
print(importancias)

# 3. Eliminação e avaliação
X_reduzido = df.drop(['ZN', 'INDUS'], axis=1)
rf2 = RandomForestRegressor().fit(X_reduzido, y)
print('Score após eliminação:', rf2.score(X_reduzido, y))
```
