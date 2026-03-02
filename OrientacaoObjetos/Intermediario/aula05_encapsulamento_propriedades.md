# Aula 05: Encapsulamento e Propriedades

## Objetivos
- Entender o conceito de encapsulamento em orientação a objetos.
- Utilizar atributos privados e protegidos em Python.
- Implementar propriedades com `@property`.

## Explicação Conceitual
### Encapsulamento
Encapsulamento é o princípio de ocultar detalhes internos de uma classe, expondo apenas o necessário para o uso externo.

### Atributos Privados e Protegidos
- Protegido: prefixo `_atributo` (convenção, acesso permitido, mas desencorajado).
- Privado: prefixo `__atributo` (name mangling, acesso restrito).

### Propriedades
Permitem controlar o acesso a atributos usando métodos getters e setters com o decorador `@property`.

## Prática com Exemplos
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo.")

conta = ContaBancaria(100)
print(conta.saldo)
conta.saldo = 200
print(conta.saldo)
conta.saldo = -50
```

## Exercícios
1. Implemente a classe `Pessoa` com atributos privados e propriedades para nome e idade.
2. Adicione validação para que a idade não seja negativa.

## Resolução dos Exercícios
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self.__idade = valor
        else:
            print("Idade não pode ser negativa.")

p = Pessoa("Ana", 30)
print(p.nome, p.idade)
p.idade = -5
```
