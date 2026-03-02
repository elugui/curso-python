# Aula 06: Modelos Supervisionados

## Explicação Conceitual
- O que são modelos supervisionados: definição e exemplos.
- Regressão linear e logística: conceitos, aplicações e diferenças.
- Árvores de decisão e Random Forest: funcionamento e vantagens.
- Métricas de avaliação: acurácia, precisão, recall, F1-score.
- Overfitting e underfitting: causas e como evitar.

## Prática com Exemplos
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Dados sintéticos para classificação
X, y = make_classification(n_samples=100, n_features=4, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Regressão logística
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
pred_log = logreg.predict(X_test)
print('Acurácia (LogReg):', accuracy_score(y_test, pred_log))

# Árvore de decisão
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
pred_tree = tree.predict(X_test)
print('Acurácia (Tree):', accuracy_score(y_test, pred_tree))

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
print('Acurácia (RF):', accuracy_score(y_test, pred_rf))

# Relatório de classificação
print(classification_report(y_test, pred_rf))
```

## Exercícios
1. Implemente um modelo de regressão logística e avalie sua acurácia.
2. Treine uma árvore de decisão e compare com Random Forest.
3. Explique o que é overfitting e como evitá-lo.

## Resolução dos Exercícios
```python
# 1. Regressão logística
from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train, y_train)
pred = logreg.predict(X_test)
print('Acurácia:', accuracy_score(y_test, pred))

# 2. Árvore vs Random Forest
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
pred_tree = tree.predict(X_test)
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
print('Acurácia Tree:', accuracy_score(y_test, pred_tree))
print('Acurácia RF:', accuracy_score(y_test, pred_rf))

# 3. Overfitting: ocorre quando o modelo aprende demais os dados de treino, perdendo capacidade de generalização. Pode ser evitado com validação cruzada, regularização e mais dados.
```
