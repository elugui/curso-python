# Aula 08: Projeto Prático Intermediário

## Explicação Conceitual
- Proposta de desafio: análise de um conjunto de dados real (ex: dados de vendas, saúde, educação).
- Aplicação do ciclo completo de Data Science: EDA, pré-processamento, modelagem, avaliação e apresentação de resultados.
- Importância da documentação e comunicação dos resultados.

## Prática com Exemplos
- Escolha um dataset público (ex: Titanic, Iris, vendas online).
- Realize EDA: estatísticas, visualizações, identificação de padrões.
- Faça o pré-processamento: tratamento de dados ausentes, normalização, codificação.
- Modele com pelo menos dois algoritmos (um supervisionado e um não supervisionado).
- Avalie os resultados e gere gráficos.

## Exercícios
1. Escolha um dataset público e realize uma análise completa, seguindo o ciclo de Data Science.
2. Documente cada etapa do processo, incluindo decisões tomadas e justificativas.
3. Apresente os resultados em um relatório ou apresentação.

## Resolução dos Exercícios
```python
# Exemplo com o dataset Titanic (disponível em seaborn)
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = sns.load_dataset('titanic')
# EDA
print(df.describe())
print(df['sex'].value_counts())
# Pré-processamento
X = df[['age', 'fare']].fillna(0)
y = df['survived'].fillna(0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Modelagem
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print('Acurácia:', accuracy_score(y_test, pred))
```
- Para a apresentação, utilize gráficos e explique as principais descobertas.
