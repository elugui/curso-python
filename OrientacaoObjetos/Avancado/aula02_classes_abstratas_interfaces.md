# Aula 02 – Classes Abstratas e Interfaces

## Explicação Conceitual
- Diferenças entre classes abstratas e interfaces
- Implementação e uso prático
- Métodos abstratos e concretos
- Aplicações em projetos reais

### Classes Abstratas
Explique o conceito, uso do módulo abc, exemplos práticos.

### Interfaces
Demonstre como simular interfaces em Python.

## Prática com Exemplos
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

q = Quadrado(4)
print(q.area())
```

## Exercícios
1. Crie uma classe abstrata Funcionario com método abstrato calcular_salario().
2. Implemente duas subclasses: Gerente e Desenvolvedor.

## Resolução dos Exercícios
```python
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def calcular_salario(self):
        return 8000

class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return 5000

g = Gerente()
d = Desenvolvedor()
print(g.calcular_salario())
print(d.calcular_salario())
```
