# Aula 05 – Exercícios Práticos: Modelando Objetos Simples

## Explicação Conceitual
Nesta aula, você irá integrar os conceitos aprendidos, modelando objetos do cotidiano e resolvendo desafios práticos.

## Prática com Exemplos
Exemplo de modelagem:
```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    # ...métodos de depósito, saque, etc...
```

## Exercícios
1. Modele uma classe "Livro" com atributos título, autor e número de páginas, e métodos para exibir informações e atualizar o número de páginas.
2. Modele uma classe "Carro" com atributos marca, modelo e ano, e métodos para exibir informações e atualizar o ano.

## Resolução dos Exercícios
```python
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def exibir(self):
        print(f"{self.titulo} - {self.autor} ({self.paginas} páginas)")
    def atualizar_paginas(self, novas_paginas):
        self.paginas = novas_paginas

livro = Livro("Python Essencial", "Carlos Lima", 200)
livro.exibir()
livro.atualizar_paginas(220)
livro.exibir()

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")
    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano

carro = Carro("Ford", "Ka", 2018)
carro.exibir()
carro.atualizar_ano(2020)
carro.exibir()
```