# Aula 07 — Visualização de Dados Básica

## Explicação Conceitual
- Importância da visualização de dados.
- Introdução ao matplotlib e seaborn.
- Tipos de gráficos: linha, barra, dispersão.

## Prática com Exemplos
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de linha
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Gráfico de Linha")
plt.show()

# Gráfico de barra
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Gráfico de Barra")
plt.show()

# Gráfico de dispersão com seaborn
sns.scatterplot(x=[1,2,3], y=[4,5,6])
plt.title("Dispersão")
plt.show()
```

## Exercícios
1. Crie um gráfico de linha mostrando a evolução de uma variável fictícia.
2. Faça um gráfico de barras com 3 categorias.
3. Explique a diferença entre matplotlib e seaborn.

## Resolução dos Exercícios
```python
import matplotlib.pyplot as plt
# Exercício 1
plt.plot([1,2,3,4], [10,20,15,25])
plt.title("Evolução da Variável")
plt.show()

# Exercício 2
plt.bar(["X", "Y", "Z"], [5, 7, 3])
plt.title("Categorias")
plt.show()

# Exercício 3
# matplotlib é mais básico e flexível, seaborn é mais focado em estatística e mais fácil para gráficos complexos.
```
