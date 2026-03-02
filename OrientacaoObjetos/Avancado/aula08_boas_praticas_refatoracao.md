# Aula 08 – Boas Práticas e Refatoração

## Explicação Conceitual
- Princípios de design
- Refatoração de código orientado a objetos
- Padrões de projeto (introdução)

### Boas Práticas
Explique princípios como SRP, DRY, KISS, YAGNI.

### Refatoração
Demonstre técnicas de refatoração em código orientado a objetos.

### Padrões de Projeto
Introduza padrões como Singleton, Factory, Observer.

## Prática com Exemplos
```python
# Exemplo de refatoração
class Calculadora:
    def somar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        return a - b

# Singleton
class Logger:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```

## Exercícios
1. Refatore uma classe que viole o SRP.
2. Implemente um padrão Singleton em Python.

## Resolução dos Exercícios
```python
# Refatoração SRP
class Usuario:
    def __init__(self, nome):
        self.nome = nome
class UsuarioDB:
    def salvar(self, usuario):
        print(f"Salvando {usuario.nome}")

# Singleton
class Config:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```
