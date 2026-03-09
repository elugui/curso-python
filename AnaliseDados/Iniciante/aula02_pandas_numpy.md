# Aula 02: Introdução ao pandas e numpy

## Objetivos
- Entender o papel das bibliotecas pandas e numpy na análise de dados.
- Conhecer as estruturas Series e DataFrame.
- Realizar operações básicas.

## Explicação Conceitual
NumPy é uma biblioteca do Python usada para computação numérica, principalmente para trabalhar com vetores, matrizes (arrays) e operações matemáticas eficientes.

Pandas é a biblioteca do Python usada para manipulação e análise de dados estruturados, permitindo organizar, limpar e analisar dados em tabelas (DataFrames), seja com poucos dados ou grandes volumes. É uma das ferramentas mais importantes para quem trabalha com análise de dados, ele facilita a manipulação de dados tabulares. 

O elemento central do Pandas são as tabelas, que são composições de colunas. No Pandas, as tabelas são o que chamamos de DataFrame e cada coluna, por sua vez, chamamos de Series. 

## Como aprender?
Pratique. Use conjuntos de dados e aplique o Pandas para fazer análises. Quanto mais praticar, mais rápido aprende.

## Prática com exemplos usando numpy
```python
import pandas as pd
import numpy as np

# Criando uma Series
ds = pd.Series([1, 2, 3, 4, 5])
print(ds)

# Criando um DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)

# Operações básicas
print(df['A'].mean())
```

### Soma de arrays
```
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
soma = a + b  # array([5, 7, 9])
```

### Média e desvio padrão
```
dados = np.array([10, 20, 30, 40])
media = np.mean(dados)         # 25.0
desvio = np.std(dados)         # 11.1803...
```

### Matriz e multiplicação de matrizes
```
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
resultado = np.matmul(mat1, mat2)
# array([[19, 22],
#        [43, 50]])
```

### Operações estatísticas
```
arr = np.array([1, 2, 3, 4, 5])
minimo = np.min(arr)           # 1
maximo = np.max(arr)           # 5
soma_total = np.sum(arr)       # 15
```

## DataFrame
DataFrame é a principal estrutura do Pandas. Ele funciona como uma tabela de dados, formada por várias Series que compartilham o mesmo índice, inspirado na linguagem R.

## Prática com exemplos usando pandas
```
import pandas as pd
from numpy.random import randn

# cria uma dataframe
df = pd.DataFrame(randn(5,4), index=["A", "B", "C", "D", "E"], columns="W X Y Z".split())
```

No código acima o método randn(5,4) para criar uma tabela de números aleatórios de cinco linhas (A, B, C, D E) por quatro colunas, definindo o índice com a sequência de letras A, B, C, D, E e a identificação para cada coluna através da string columns=“W X Y Z”.split(). O método split() quebra essa string em uma lista de strings. 

### Seleção e indexação
```
# retorna a coluna chamada "W" do DataFrame df. O resultado é uma Series do pandas.
df['W']
```

```
# retorna, do DataFrame df, apenas as colunas "W" e "Z" ao mesmo tempo. 
# O resultado é um novo DataFrame contendo somente essas duas colunas e todas as linhas originais.
df[['W','Z']]
```

> ***Dica:*** O comando type() em Python mostra o tipo do objeto passado como argumento. Por exemplo, type(df['W']) indica que df['W'] é uma Series do pandas, enquanto type(df[['W','Z']]) mostra que df[['W','Z']] é um DataFrame do pandas. Isso ajuda a identificar a estrutura dos dados que você está manipulando.

```
type(df['W'])
type(df[['W','Z']])
```

**Criando uma nova coluna:**
```
df['new'] = df['W'] + df['Y']
```

**Removendo uma coluna:**
```
# O comando df.drop('new', axis=1) remove a coluna 'new' do DataFrame df e retorna um novo DataFrame
# sem essa coluna. O df original não é alterado.
df.drop('new',axis=1)
```

```
# O comando df.drop('new', axis=1, inplace=True) remove a coluna 'new' do DataFrame df e altera o 
# próprio df, ou seja, a exclusão é feita diretamente no objeto original, sem necessidade de criar um
# novo DataFrame.
df.drop('new',axis=1,inplace=True)
```

```
# O comando df.drop('E', axis=0) retorna um novo DataFrame igual ao df, mas sem a linha cujo índice é
# 'E'. O parâmetro axis=0 indica que a remoção é feita em linhas. O df original não é alterado, a
# menos que você use inplace=True.
df.drop('E',axis=0)
```

No pandas, o parâmetro axis define se a operação será feita em linhas ou colunas:

- **axis=0:** a operação é feita nas linhas (por exemplo, remove uma linha).
- **axis=1:** a operação é feita nas colunas (por exemplo, remove uma coluna).

**Selecionando linhas:**
O comando df.loc['A'] seleciona e retorna todos os dados da linha cujo índice é 'A' no DataFrame df. O resultado é uma Series contendo os valores dessa linha, com os nomes das colunas como índice.
```
df.loc['A']
```

Outra opção é selecionar com base na posição em vez do rótulo:
```
df.iloc[2]
```

O comando df.iloc[0, 2] seleciona o valor que está na primeira linha (índice 0) e na terceira coluna (índice 2) do DataFrame df, usando indexação baseada em posição (e não nos nomes dos índices ou colunas).

Ou seja, iloc permite acessar elementos do DataFrame pelo número da linha e da coluna, começando do zero. Por exemplo, se df tem as colunas ['A', 'B', 'C'], então df.iloc[0, 2] retorna o valor da primeira linha e da coluna 'C'.
```
df.iloc[0, 2]
```

O comando df.loc['B', 'Y'] retorna o valor específico que está na linha de índice 'B' e na coluna 'Y' do DataFrame df. Ou seja, ele acessa diretamente o dado na interseção dessa linha e coluna.
```
df.loc['B','Y']
```

O comando df.loc[['A','B'], ['W','Y']] seleciona, do DataFrame df, as linhas de índice 'A' e 'B' e, dessas linhas, apenas as colunas 'W' e 'Y'. O resultado é um novo DataFrame contendo esse subconjunto de dados.
```
df.loc[['A','B'],['W','Y']]
```

**Criando uma nova coluna**
A linha df['new'] = df['W'] + df['Y'] cria uma nova coluna chamada new no DataFrame df, somando os valores das colunas W e Y em cada linha.
```
df['new'] = df['W'] + df['Y']
```

## Seleção condicional
Seleção condicional em DataFrames permite filtrar dados com base em condições, como valores maiores que zero ou iguais a um critério. É útil para analisar, visualizar ou manipular apenas parte dos dados que atendem a certas regras, facilitando a extração de informações relevantes.

Esse comando retorna um DataFrame com True onde o valor é maior que 0 e False onde não é.
```
df > 0
```

Esse comando mostra apenas os valores maiores que 0 no DataFrame; os outros aparecem como NaN (vazio).
```
df[df>0]
```

Esse comando retorna apenas as linhas do DataFrame onde a coluna W tem valor maior que 0.
```
df[df['W']>0]
```

Esse comando retorna apenas os valores da coluna Y para as linhas onde a coluna W é maior que 0.
```
df[df['W']>0]['Y']
```

Esse comando mostra apenas as colunas Y e X das linhas onde a coluna W é maior que 0.
```
df[df['W']>0][['Y','X']]
```

Esse comando retorna apenas as linhas em que a coluna W é maior que 0 e a coluna Y é maior que 1 ao mesmo tempo.
```
df[(df['W']>0) & (df['Y'] > 1)]
```

Aqui, as condições são salvas em variáveis (condicao_1 e condicao_2). Depois, essas variáveis são usadas para filtrar o DataFrame, mostrando só as linhas onde ambas as condições são verdadeiras. Isso deixa o código mais organizado e fácil de entender.
```
condicao_1 = df['W'] > 0
condicao_2 = df['Y'] > 1

df[(condicao_1) & (condicao_2)]
```

Esse comando usa o operador | (ou) para combinar as duas condições salvas nas variáveis. Ele retorna as linhas do DataFrame onde pelo menos uma das condições é
```
df[(condicao_1) | (condicao_2)]
```
