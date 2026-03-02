# Aula 03: Composição e Agregação

## Objetivos
- Diferenciar composição e agregação em orientação a objetos.
- Aplicar composição e agregação em projetos Python.

## Explicação Conceitual
### Composição
Composição é uma relação forte onde uma classe "possui" outra. Se o objeto principal for destruído, os objetos componentes também são.

### Agregação
Agregação é uma relação mais fraca, onde uma classe utiliza outra, mas os objetos podem existir independentemente.

## Prática com Exemplos
#### Composição
```python
class Motor:
    def ligar(self):
        print("Motor ligado!")

class Carro:
    def __init__(self):
        self.motor = Motor()
    def ligar(self):
        self.motor.ligar()

carro = Carro()
carro.ligar()
```
#### Agregação
```python
class Departamento:
    def __init__(self, nome):
        self.nome = nome

class Funcionario:
    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento

dep = Departamento("TI")
func = Funcionario("Ana", dep)
print(func.departamento.nome)
```

## Exercícios
1. Implemente uma classe `Livro` que possui uma composição com a classe `Autor`.
2. Implemente uma classe `Turma` que agrega objetos da classe `Aluno`.

## Resolução dos Exercícios
```python
# Composição
class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor_nome):
        self.titulo = titulo
        self.autor = Autor(autor_nome)

livro = Livro("Python OOP", "Carlos")
print(livro.autor.nome)

# Agregação
class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self):
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

a1 = Aluno("João")
a2 = Aluno("Maria")
turma = Turma()
turma.adicionar_aluno(a1)
turma.adicionar_aluno(a2)
for aluno in turma.alunos:
    print(aluno.nome)
```
