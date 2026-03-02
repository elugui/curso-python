# Aula 05: Machine Learning Interpretável

## Explicação Conceitual
- O que é interpretabilidade em modelos de ML.
- Ferramentas: SHAP, LIME.
- Diferença entre interpretabilidade e explicabilidade.
- Trade-off entre interpretabilidade e acurácia.

## Prática com Exemplos
```python
import shap
import xgboost
from sklearn.datasets import load_boston

# Treinar modelo XGBoost
X, y = load_boston(return_X_y=True)
model = xgboost.XGBRegressor().fit(X, y)

# SHAP
explainer = shap.Explainer(model)
shap_values = explainer(X)
shap.summary_plot(shap_values, X)

# LIME (exemplo conceitual)
# from lime.lime_tabular import LimeTabularExplainer
# explainer = LimeTabularExplainer(X)
# explanation = explainer.explain_instance(X[0], model.predict)
# explanation.show_in_notebook()
```

## Exercícios
1. Explique a importância da interpretabilidade em ML.
2. Utilize SHAP para interpretar um modelo de regressão.
3. Compare SHAP e LIME em termos de aplicação e resultados.

## Resolução dos Exercícios
```python
# 1. Importância: permite entender decisões do modelo, identificar vieses e aumentar confiança.
# 2. SHAP já demonstrado acima.
# 3. SHAP: baseado em teoria dos jogos, global e local; LIME: aproximação local, mais simples de usar.
```
