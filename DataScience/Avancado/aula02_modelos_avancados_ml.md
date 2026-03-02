# Aula 02: Modelos Avançados de Machine Learning

## Explicação Conceitual
- O que são ensemble methods: combinação de modelos para melhorar desempenho.
- Principais algoritmos: Gradient Boosting, XGBoost, LightGBM.
- Introdução a redes neurais: perceptron, camadas, funções de ativação.
- Ajuste de hiperparâmetros: grid search, random search.

## Prática com Exemplos
```python
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Gradient Boosting
gb = GradientBoostingClassifier().fit(X_train, y_train)
print('Acurácia GB:', gb.score(X_test, y_test))

# XGBoost
xgb = XGBClassifier(eval_metric='logloss').fit(X_train, y_train)
print('Acurácia XGB:', xgb.score(X_test, y_test))

# LightGBM
lgbm = LGBMClassifier().fit(X_train, y_train)
print('Acurácia LGBM:', lgbm.score(X_test, y_test))

# Grid Search para hiperparâmetros
params = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
gs = GridSearchCV(gb, params, cv=3).fit(X_train, y_train)
print('Melhores parâmetros:', gs.best_params_)
```

## Exercícios
1. Treine um modelo Gradient Boosting e avalie sua acurácia.
2. Compare os resultados de XGBoost e LightGBM.
3. Realize ajuste de hiperparâmetros usando GridSearchCV.

## Resolução dos Exercícios
```python
# 1. Gradient Boosting
model = GradientBoostingClassifier().fit(X_train, y_train)
print(model.score(X_test, y_test))

# 2. XGBoost vs LightGBM
xgb = XGBClassifier(eval_metric='logloss').fit(X_train, y_train)
lgbm = LGBMClassifier().fit(X_train, y_train)
print('XGB:', xgb.score(X_test, y_test), 'LGBM:', lgbm.score(X_test, y_test))

# 3. Grid Search
params = {'n_estimators': [10, 50]}
gs = GridSearchCV(model, params, cv=2).fit(X_train, y_train)
print(gs.best_params_)
```
