# Aula 1: Estruturas de Dados Avançadas

## Introdução Conceitual
Dicionários, conjuntos e tuplas são estruturas fundamentais para organizar e manipular dados em Python:
- **Dicionários** armazenam pares chave-valor, ideais para buscas rápidas e organização de dados relacionais.
- **Conjuntos** são coleções não ordenadas de elementos únicos, úteis para eliminar duplicatas e realizar operações matemáticas de conjuntos.
- **Tuplas** são sequências imutáveis, ótimas para representar dados fixos ou retornos múltiplos de funções.

## Exemplos Práticos
### Dicionários
```python
aluno = {"nome": "Ana", "idade": 20, "curso": "Python"}
print(aluno["nome"])  # Acessando valor pela chave
aluno["idade"] = 21    # Alterando valor
```

### Conjuntos
```python
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(numeros)
print(conjunto)  # {1, 2, 3, 4, 5}
```

### Tuplas
```python
def coordenadas():
    return (10, 20)
x, y = coordenadas()
print(f"x={x}, y={y}")
```

## Exercícios Propostos
1. Crie um dicionário para armazenar nome e nota de 3 alunos e imprima a média das notas.
2. Dada uma lista com números repetidos, use um conjunto para mostrar apenas os valores únicos.
3. Escreva uma função que recebe dois números e retorna uma tupla com a soma e o produto deles.

## Resolução dos Exercícios
### 1. Dicionário de alunos
```python
alunos = {"João": 7.5, "Maria": 8.0, "Pedro": 6.5}
media = sum(alunos.values()) / len(alunos)
print(f"Média: {media:.2f}")
```

### 2. Conjunto de valores únicos
```python
lista = [1, 2, 2, 3, 4, 4, 5]
unicos = set(lista)
print(unicos)
```

### 3. Função com tupla
```python
def soma_produto(a, b):
    return (a + b, a * b)
resultado = soma_produto(3, 4)
print(f"Soma: {resultado[0]}, Produto: {resultado[1]}")
```

## Boas Práticas
- Use nomes de chaves e variáveis claros.
- Prefira tuplas para dados imutáveis e conjuntos para eliminar duplicatas.
- Consulte a documentação oficial para métodos úteis de cada estrutura.