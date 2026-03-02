# Aula 03: Introdução à Estatística para Data Science

## Explicação Conceitual
- Estatística descritiva vs. inferencial
- Distribuições de probabilidade: normal, binomial, Poisson
- Testes de hipóteses: conceito, erro tipo I e II
- Correlação e regressão: relação entre variáveis

## Prática com Exemplos
```python
import numpy as np
import scipy.stats as stats
# Distribuição normal
dados = np.random.normal(loc=50, scale=10, size=100)
print('Média:', np.mean(dados))
print('Desvio padrão:', np.std(dados))

# Teste de hipótese (t-test)
grupo1 = np.random.normal(50, 10, 30)
grupo2 = np.random.normal(55, 10, 30)
t_stat, p_val = stats.ttest_ind(grupo1, grupo2)
print('t-stat:', t_stat, 'p-value:', p_val)

# Correlação
x = np.arange(10)
y = 2 * x + np.random.normal(0, 1, 10)
correlacao = np.corrcoef(x, y)[0, 1]
print('Correlação:', correlacao)
```

## Exercícios
1. Gere uma amostra de dados com distribuição normal e calcule média e desvio padrão.
2. Realize um teste t para comparar dois grupos.
3. Calcule a correlação entre duas variáveis.

## Resolução dos Exercícios
```python
# 1. Amostra normal
dados = np.random.normal(100, 15, 50)
print('Média:', np.mean(dados))
print('Desvio padrão:', np.std(dados))

# 2. Teste t
g1 = np.random.normal(100, 10, 20)
g2 = np.random.normal(110, 10, 20)
t, p = stats.ttest_ind(g1, g2)
print('t:', t, 'p:', p)

# 3. Correlação
x = np.random.rand(30)
y = 3 * x + np.random.normal(0, 0.5, 30)
print('Correlação:', np.corrcoef(x, y)[0, 1])
```
