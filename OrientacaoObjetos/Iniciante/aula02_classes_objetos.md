# Aula 02 – Classes e Objetos em Python

## Explicação Conceitual
Classe é um molde para criar objetos. Um objeto é uma instância de uma classe. Atributos são características e métodos são comportamentos.

## Prática com Exemplos
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco}")

# Criando um objeto
p1 = Produto("Caneta", 2.5)
p1.exibir()
```

## Exercícios
1. Crie uma classe chamada "Animal" com atributos nome e espécie, e um método para exibir essas informações.
2. Instancie dois objetos da classe "Animal" e chame o método de exibição.

## Resolução dos Exercícios
```python
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def exibir(self):
        print(f"Nome: {self.nome}, Espécie: {self.especie}")

# Instanciando objetos
animal1 = Animal("Rex", "Cachorro")
animal2 = Animal("Mimi", "Gato")
animal1.exibir()
animal2.exibir()
```