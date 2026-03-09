# Aula 06 — Mini-projeto: Análise de Dados Reais

## Objetivos
- Aplicar os conhecimentos adquiridos em um projeto prático.

## Explicação Conceitual
Projetos práticos consolidam o aprendizado, simulando situações reais de análise de dados.

### Proposta de Projeto
- Escolha um dataset público (ex: Kaggle, IBGE, dados.gov.br)
- Realize limpeza, manipulação, análise estatística e visualização
- Apresente conclusões

## Prática com Exemplos
1. Baixe um dataset público.
2. Realize as etapas de limpeza, análise e visualização.

## Exercícios
1. Escolha um dataset, realize todas as etapas do processo de análise e apresente um relatório final.

## Resolução dos Exercícios
```python
# Exemplo de etapas
import pandas as pd
# 1. Carregar dados
df = pd.read_csv('dataset.csv')
# 2. Limpeza
df = df.dropna()
# 3. Análise estatística
df.describe()
# 4. Visualização
df.plot.hist()
```
