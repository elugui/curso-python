# Aula 08 — Projeto Prático

## Explicação Conceitual
- O que é análise exploratória de dados (EDA)?
- Etapas de um projeto de Data Science.
- Importância da documentação e apresentação dos resultados.

## Prática com Exemplos
- Escolha de um dataset simples (ex: Titanic, Iris, vendas fictícias).
- Passos: leitura dos dados, análise inicial, visualização básica, conclusões.

## Exercícios
1. Escolha um dataset simples e faça uma análise exploratória inicial (leitura, estatísticas básicas, gráficos simples).
2. Documente suas conclusões principais.

## Resolução dos Exercícios
- Exemplo de análise com o dataset Iris:
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.describe())
sns.pairplot(df, hue="species")
plt.show()
```
- Conclusão exemplo: "As espécies de íris apresentam diferenças claras nas medidas das pétalas e sépalas."
