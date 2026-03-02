# Aula 04: Métodos Especiais e Sobrecarga

## Objetivos
- Compreender o papel dos métodos especiais em Python.
- Implementar métodos como `__str__`, `__repr__`, `__eq__`, `__add__`.
- Entender o conceito de sobrecarga de operadores.

## Explicação Conceitual
### Métodos Especiais
Métodos especiais são funções com nomes entre duplo sublinhado (dunder methods), que permitem customizar o comportamento de objetos (ex: impressão, comparação, soma).

### Sobrecarga de Operadores
Permite redefinir operadores (como +, ==) para objetos de classes definidas pelo usuário.

## Prática com Exemplos
```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = p1 + p2
print(p3)
print(p1 == p2)
```

## Exercícios
1. Implemente a classe `Produto` com métodos especiais para exibição (`__str__`), comparação (`__eq__`) e soma de preços (`__add__`).
2. Crie exemplos de uso desses métodos.

## Resolução dos Exercícios
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    def __eq__(self, outro):
        return self.nome == outro.nome and self.preco == outro.preco
    def __add__(self, outro):
        return self.preco + outro.preco

p1 = Produto("Caneta", 2.5)
p2 = Produto("Lápis", 1.5)
p3 = Produto("Caneta", 2.5)
print(p1)
print(p1 == p3)
print(p1 + p2)
```
