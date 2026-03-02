# Aula 02: Geradores e Iteradores

## 1. Explicações Conceituais

- **Geradores:** Funções que usam `yield` para produzir uma sequência de valores sob demanda.
- **Iteradores:** Objetos que implementam os métodos `__iter__()` e `__next__()`.
- **Uso prático:** Economia de memória ao lidar com grandes volumes de dados.

## 2. Práticas com Exemplos

### Gerador simples
```python
def contador():
    for i in range(5):
        yield i

for numero in contador():
    print(numero)
```

### Iterador personalizado
```python
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.atual < self.limite:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration

for n in Contador(3):
    print(n)
```

## 3. Exercícios

1. Crie um gerador que produza os números pares de 0 a 10.
2. Implemente um iterador que percorra uma lista de trás para frente.
3. Use um gerador para ler um arquivo linha a linha.

## 4. Resolução dos Exercícios

### Exercício 1
```python
def pares():
    for i in range(0, 11, 2):
        yield i
```

### Exercício 2
```python
class Reverso:
    def __init__(self, lista):
        self.lista = lista
        self.indice = len(lista)
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == 0:
            raise StopIteration
        self.indice -= 1
        return self.lista[self.indice]
```

### Exercício 3
```python
def ler_arquivo(nome):
    with open(nome) as f:
        for linha in f:
            yield linha.strip()
```
