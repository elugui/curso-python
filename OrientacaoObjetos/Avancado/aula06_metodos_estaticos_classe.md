# Aula 06 – Métodos Estáticos e de Classe

## Explicação Conceitual
- Diferença entre métodos estáticos e de classe
- Quando usar cada um
- Exemplos práticos

### Métodos Estáticos
Explique o uso do decorator @staticmethod.

### Métodos de Classe
Demonstre o uso do decorator @classmethod.

## Prática com Exemplos
```python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    @classmethod
    def dobro(cls, valor):
        return valor * 2

print(Matematica.somar(2, 3))
print(Matematica.dobro(4))
```

## Exercícios
1. Implemente uma classe Conversor com métodos estáticos para conversão de unidades.
2. Implemente um método de classe para contar instâncias criadas.

## Resolução dos Exercícios
```python
class Conversor:
    instancias = 0
    def __init__(self):
        Conversor.instancias += 1
    @staticmethod
    def km_para_milhas(km):
        return km * 0.621371
    @classmethod
    def total_instancias(cls):
        return cls.instancias

c1 = Conversor()
c2 = Conversor()
print(Conversor.km_para_milhas(10))
print(Conversor.total_instancias())
```
