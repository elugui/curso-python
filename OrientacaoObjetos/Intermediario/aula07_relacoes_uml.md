# Aula 07: Relações entre Objetos e UML

## Objetivos
- Compreender diferentes tipos de relações entre objetos (associação, dependência, composição, agregação).
- Representar essas relações usando diagramas UML.

## Explicação Conceitual
### Associação
Relação onde objetos se conhecem e podem interagir.

### Dependência
Uma classe depende de outra para realizar uma ação.

### Composição e Agregação
Já estudadas em aulas anteriores, são relações de "parte-todo" com diferentes níveis de dependência.

### UML
A UML (Unified Modeling Language) é uma linguagem padrão para modelar sistemas orientados a objetos.

## Prática com Exemplos
```python
class Professor:
    def __init__(self, nome):
        self.nome = nome

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor  # Associação

def matricular(aluno, disciplina):  # Dependência
    print(f"{aluno} matriculado em {disciplina.nome}")

prof = Professor("Carlos")
disc = Disciplina("Matemática", prof)
matricular("Ana", disc)
```

## Exercícios
1. Modele uma relação de associação entre as classes `Cliente` e `Pedido`.
2. Represente a relação entre `Departamento` e `Funcionario` usando UML.

## Resolução dos Exercícios
```python
# Associação
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []
    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

class Pedido:
    def __init__(self, descricao):
        self.descricao = descricao

cliente = Cliente("João")
pedido = Pedido("Pizza")
cliente.adicionar_pedido(pedido)
print(cliente.pedidos[0].descricao)
```

### UML (exemplo simplificado)
```
+----------------+        +----------------+
| Departamento   |<>----- | Funcionario    |
+----------------+        +----------------+
| nome           |        | nome           |
+----------------+        +----------------+
```
