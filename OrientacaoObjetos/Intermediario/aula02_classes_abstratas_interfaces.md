# Aula 02: Classes Abstratas e Interfaces

## Objetivos
- Entender o conceito de classes abstratas e interfaces em Python.
- Utilizar o módulo `abc` para criar classes abstratas.
- Implementar métodos abstratos em subclasses.

## Explicação Conceitual
### Classes Abstratas
Classes abstratas servem como modelos para outras classes. Não podem ser instanciadas diretamente e podem definir métodos que devem ser implementados pelas subclasses.

### Interfaces
Em Python, interfaces são simuladas por classes abstratas que possuem apenas métodos abstratos.

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
1. Crie uma classe abstrata `Funcionario` com um método abstrato `calcular_salario`.
2. Implemente duas subclasses: `FuncionarioCLT` e `FuncionarioPJ`, cada uma com sua própria lógica de cálculo de salário.

## Resolução dos Exercícios
```python
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, salario_base):
        self.salario_base = salario_base
    def calcular_salario(self):
        return self.salario_base

class FuncionarioPJ(Funcionario):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora
    def calcular_salario(self):
        return self.horas * self.valor_hora

clt = FuncionarioCLT(3000)
pj = FuncionarioPJ(160, 30)
print(clt.calcular_salario())
print(pj.calcular_salario())
```
