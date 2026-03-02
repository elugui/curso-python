# Aula 04: Machine Learning – Fundamentos

## Explicação Conceitual
- O que é Machine Learning (ML): definição e aplicações.
- Tipos de aprendizado: supervisionado, não supervisionado, por reforço.
- Pipeline básico de ML: coleta de dados, pré-processamento, modelagem, avaliação e implantação.
- Principais algoritmos: regressão, classificação, clustering.

## Prática com Exemplos
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Carregar dados
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Treinar modelo
modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)

# Avaliar modelo
pred = modelo.predict(X_test)
print('Acurácia:', accuracy_score(y_test, pred))
```

## Exercícios
1. Explique a diferença entre aprendizado supervisionado e não supervisionado.
2. Implemente um modelo de classificação simples usando scikit-learn.
3. Descreva as etapas de um pipeline de ML.

## Resolução dos Exercícios
```python
# 2. Modelo de classificação
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print('Acurácia:', accuracy_score(y_test, pred))

# 1 e 3 são respostas conceituais:
# 1. Supervisionado: usa dados rotulados; Não supervisionado: não usa rótulos.
# 3. Coleta de dados, pré-processamento, modelagem, avaliação, implantação.
```
