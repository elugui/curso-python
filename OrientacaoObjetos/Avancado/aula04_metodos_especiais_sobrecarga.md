# Aula 04 – Métodos Especiais e Sobrecarga

## Explicação Conceitual
- Métodos dunder (__init__, __str__, etc.)
- Sobrecarga de operadores
- Customização de comportamento de classes

### Métodos Especiais
Explique o conceito de métodos especiais (dunder), exemplos práticos.

### Sobrecarga de Operadores
Demonstre como sobrecarregar operadores em Python.

## Prática com Exemplos
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return f"Pessoa: {self.nome}"
    def __eq__(self, other):
        return self.nome == other.nome

p1 = Pessoa("Ana")
p2 = Pessoa("Ana")
print(p1)
print(p1 == p2)
```

## Exercícios
1. Implemente uma classe Produto com métodos __str__ e __eq__.
2. Implemente a soma de dois objetos Produto (sobrecarga de __add__).

## Resolução dos Exercícios
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"Produto: {self.nome} - R$ {self.preco}"
    def __eq__(self, other):
        return self.nome == other.nome and self.preco == other.preco
    def __add__(self, other):
        return Produto(self.nome + ' & ' + other.nome, self.preco + other.preco)

p1 = Produto("Caneta", 2)
p2 = Produto("Lápis", 1)
p3 = p1 + p2
print(p3)
```
