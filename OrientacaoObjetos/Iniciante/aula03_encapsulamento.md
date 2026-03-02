# Aula 03 – Encapsulamento e Atributos de Instância

## Explicação Conceitual
Encapsulamento é o princípio de esconder detalhes internos do objeto, expondo apenas o necessário. Em Python, usamos o prefixo _ para indicar atributos protegidos e __ para privados.

## Prática com Exemplos
```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # protegido
        self.__idade = idade  # privado

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
```

## Exercícios
1. Implemente uma classe "ContaBancaria" com atributo privado saldo e métodos para depositar, sacar e consultar saldo.

## Resolução dos Exercícios
```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

# Exemplo de uso
conta = ContaBancaria("João")
conta.depositar(100)
conta.sacar(30)
print(conta.consultar_saldo())  # 70
```