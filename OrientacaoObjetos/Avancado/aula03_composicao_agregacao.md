# Aula 03 – Composição e Agregação

## Explicação Conceitual
- Diferença entre composição e agregação
- Vantagens e desvantagens
- Exemplos práticos
- Modelagem de relacionamentos complexos

### Composição
Explique o conceito, exemplos de classes que possuem outras classes como atributos.

### Agregação
Demonstre agregação, onde objetos podem existir independentemente.

## Prática com Exemplos
```python
class Motor:
    def ligar(self):
        print("Motor ligado.")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Composição
    def ligar(self):
        self.motor.ligar()

carro = Carro()
carro.ligar()
```

## Exercícios
1. Modele uma classe Departamento que possui vários Funcionarios (composição).
2. Modele uma classe Turma que agrega vários Alunos (agregação).

## Resolução dos Exercícios
```python
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self):
        self.funcionarios = []
    def adicionar(self, funcionario):
        self.funcionarios.append(funcionario)

dep = Departamento()
dep.adicionar(Funcionario("Ana"))
dep.adicionar(Funcionario("João"))
for f in dep.funcionarios:
    print(f.nome)

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self):
        self.alunos = []
    def adicionar(self, aluno):
        self.alunos.append(aluno)

turma = Turma()
aluno1 = Aluno("Carlos")
aluno2 = Aluno("Maria")
turma.adicionar(aluno1)
turma.adicionar(aluno2)
for a in turma.alunos:
    print(a.nome)
```
