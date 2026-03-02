# Aula 05 – Encapsulamento e Propriedades

## Explicação Conceitual
- Encapsulamento avançado
- Propriedades (property)
- Getters, setters e deleters
- Controle de acesso

### Encapsulamento
Explique o conceito, uso de atributos privados e protegidos.

### Propriedades
Demonstre o uso do decorator @property para controle de acesso.

## Prática com Exemplos
```python
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor

conta = ContaBancaria(100)
print(conta.saldo)
conta.saldo = 200
print(conta.saldo)
```

## Exercícios
1. Implemente uma classe Pessoa com atributo privado _idade e propriedade idade.
2. Crie métodos para validar a idade (não pode ser negativa).

## Resolução dos Exercícios
```python
class Pessoa:
    def __init__(self, idade):
        self._idade = idade
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else:
            raise ValueError("Idade não pode ser negativa.")

p = Pessoa(30)
print(p.idade)
p.idade = 40
print(p.idade)
```
