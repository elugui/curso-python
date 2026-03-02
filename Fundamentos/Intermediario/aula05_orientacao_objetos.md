# Aula 5: Introdução à Orientação a Objetos

## Introdução Conceitual
A programação orientada a objetos (POO) organiza o código em torno de "objetos", que combinam dados e comportamentos. Os principais conceitos são:
- **Classe**: molde para criar objetos.
- **Objeto**: instância de uma classe.
- **Atributos**: características do objeto.
- **Métodos**: comportamentos do objeto.
- **Herança**: permite criar novas classes baseadas em outras.

## Exemplos Práticos
### Definindo uma Classe
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"{self.nome}: R$ {self.preco:.2f}")

p = Produto('Caneta', 2.5)
p.exibir()
```

### Herança
```python
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

c = Carro('Ford', 'Ka')
print(c.marca, c.modelo)
```

## Exercícios Propostos
1. Crie uma classe `Aluno` com atributos nome e nota, e um método para exibir os dados.
2. Implemente uma classe `Funcionario` e uma subclasse `Gerente` que herda de `Funcionario`.

## Resolução dos Exercícios
### 1. Classe Aluno
```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def exibir(self):
        print(f"Aluno: {self.nome}, Nota: {self.nota}")

aluno = Aluno('Lucas', 9.0)
aluno.exibir()
```

### 2. Herança Funcionario/Gerente
```python
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Gerente(Funcionario):
    def __init__(self, nome, setor):
        super().__init__(nome)
        self.setor = setor

g = Gerente('Paula', 'TI')
print(g.nome, g.setor)
```

## Boas Práticas
- Nomeie classes com maiúscula inicial.
- Use herança apenas quando fizer sentido.
- Separe código em módulos para organização.