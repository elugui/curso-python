# Aula 06: Mini-projeto: Análise Exploratória de um Dataset Simples

## Objetivos
- Aplicar os conceitos aprendidos em um dataset real.

## Explicação Conceitual
Análise exploratória: entender, limpar, visualizar e tirar conclusões dos dados.

## Prática com Exemplos
Escolha um dataset simples (ex: vendas, notas de alunos). Realize leitura, limpeza, análise e visualização.

## Exercícios
1. Baixe um dataset público simples e realize uma análise exploratória.
2. Apresente um resumo dos principais achados.

## Resolução dos Exercícios
- Passo a passo guiado, com exemplos de código para cada etapa:
```python
import pandas as pd
import matplotlib.pyplot as plt
# Leitura do dataset
df = pd.read_csv('notas_alunos.csv')
# Limpeza básica
df = df.dropna()
# Análise descritiva
print(df.describe())
# Visualização
df['nota'].plot(kind='hist')
plt.show()
```