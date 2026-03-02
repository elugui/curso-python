# Aula 06: Classes e Métodos Estáticos

## Objetivos
- Compreender a diferença entre métodos de instância, estáticos e de classe.
- Utilizar `@staticmethod` e `@classmethod` em Python.

## Explicação Conceitual
### Métodos de Instância
Acessam e modificam atributos do objeto (self).

### Métodos Estáticos
Não acessam nem modificam atributos da instância ou da classe. Utilizam o decorador `@staticmethod`.

### Métodos de Classe
Acessam/modificam atributos da classe. Utilizam o decorador `@classmethod` e recebem `cls` como primeiro parâmetro.

## Prática com Exemplos
```python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    @classmethod
    def info(cls):
        return f"Classe: {cls.__name__}"

print(Matematica.somar(2, 3))
print(Matematica.info())
```

## Exercícios
1. Implemente uma classe `ConversorTemperatura` com métodos estáticos para converter Celsius para Fahrenheit e vice-versa.
2. Adicione um método de classe que retorna o nome da classe.

## Resolução dos Exercícios
```python
class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(c):
        return c * 9/5 + 32
    @staticmethod
    def fahrenheit_para_celsius(f):
        return (f - 32) * 5/9
    @classmethod
    def nome_classe(cls):
        return cls.__name__

print(ConversorTemperatura.celsius_para_fahrenheit(0))
print(ConversorTemperatura.fahrenheit_para_celsius(32))
print(ConversorTemperatura.nome_classe())
```
