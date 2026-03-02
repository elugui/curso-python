# Aula 01: Programação Funcional em Python

## 1. Explicações Conceituais

- **Funções de alta ordem:** Funções que recebem outras funções como argumento ou retornam funções.
- **Funções lambda avançadas:** Funções anônimas para operações rápidas.
- **Map, filter, reduce:** Ferramentas para processamento funcional de coleções.
- **Decoradores:** Funções que modificam o comportamento de outras funções.

## 2. Práticas com Exemplos

### Funções de alta ordem
```python
def aplicar_operacao(func, lista):
    return [func(x) for x in lista]

print(aplicar_operacao(lambda x: x**2, [1, 2, 3]))
```

### Map, filter, reduce
```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
soma = reduce(lambda x, y: x + y, numeros)
print(quadrados, pares, soma)
```

### Decoradores
```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print('Antes da função')
        resultado = func(*args, **kwargs)
        print('Depois da função')
        return resultado
    return wrapper

@meu_decorador
def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Python')
```

## 3. Exercícios

1. Crie uma função de alta ordem que recebe uma lista e uma função, e retorna uma nova lista com a função aplicada a cada elemento.
2. Use `map` para converter uma lista de temperaturas em Celsius para Fahrenheit.
3. Use `filter` para filtrar números ímpares de uma lista.
4. Crie um decorador que imprime o tempo de execução de uma função.

## 4. Resolução dos Exercícios

### Exercício 1
```python
def aplicar_funcao(lista, func):
    return [func(x) for x in lista]
```

### Exercício 2
```python
temperaturas_c = [0, 20, 30]
temperaturas_f = list(map(lambda c: c * 9/5 + 32, temperaturas_c))
```

### Exercício 3
```python
numeros = [1, 2, 3, 4, 5]
impares = list(filter(lambda x: x % 2 != 0, numeros))
```

### Exercício 4
```python
import time

def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f'Tempo: {fim - inicio:.4f}s')
        return resultado
    return wrapper
```
