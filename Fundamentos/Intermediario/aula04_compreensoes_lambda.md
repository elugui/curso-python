# Aula 4: Compreensões de Listas e Expressões Lambda

## Introdução Conceitual
Compreensões de listas e funções lambda permitem escrever código mais conciso e expressivo:
- **List comprehensions**: criam listas a partir de iteráveis de forma compacta.
- **Lambda**: funções anônimas, geralmente usadas para operações simples.
- **map, filter, reduce**: funções de programação funcional para processar coleções.

## Exemplos Práticos
### List Comprehension
```python
quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]
```

### Lambda e map
```python
numeros = [1, 2, 3]
dobro = list(map(lambda x: x*2, numeros))
print(dobro)
```

### filter e reduce
```python
pares = list(filter(lambda x: x%2==0, range(10)))
print(pares)

from functools import reduce
soma = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(soma)
```

## Exercícios Propostos
1. Use list comprehension para criar uma lista com os cubos dos números de 1 a 10.
2. Filtre os números pares de uma lista usando filter e lambda.
3. Some todos os elementos de uma lista usando reduce.

## Resolução dos Exercícios
### 1. Cubos com list comprehension
```python
cubos = [x**3 for x in range(1, 11)]
print(cubos)
```

### 2. Filtrar pares
```python
lista = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)
```

### 3. Soma com reduce
```python
from functools import reduce
soma = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(soma)
```

## Boas Práticas
- Use list comprehensions para clareza e performance.
- Prefira lambda para funções simples e rápidas.
- Evite expressões muito complexas em uma única linha.