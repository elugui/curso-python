# Aula 09: Projeto Prático Orientado a Objetos

## Objetivos
- Aplicar todos os conceitos de orientação a objetos em um projeto prático.
- Desenvolver um sistema simples utilizando herança, polimorfismo, composição, encapsulamento, métodos especiais, etc.

## Explicação Conceitual
Nesta aula, o objetivo é integrar todos os conceitos estudados em um projeto prático, reforçando a importância do design orientado a objetos.

## Proposta de Projeto
Desenvolva um sistema de gerenciamento de biblioteca:
- Classes: `Livro`, `Usuario`, `Biblioteca`, `Emprestimo`.
- Relacionamentos: associação, composição, agregação.
- Encapsulamento, propriedades, métodos especiais.

## Prática com Exemplos
```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Usuario:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
    def __str__(self):
        return f"{self.usuario} pegou {self.livro}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    def emprestar_livro(self, livro, usuario):
        emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(emprestimo)
        self.livros.remove(livro)

biblio = Biblioteca()
livro1 = Livro("Python Básico", "Ana")
usuario1 = Usuario("Carlos")
biblio.adicionar_livro(livro1)
biblio.emprestar_livro(livro1, usuario1)
for emp in biblio.emprestimos:
    print(emp)
```

## Exercícios
1. Expanda o sistema para permitir devolução de livros.
2. Adicione validações para não emprestar livros indisponíveis.

## Resolução dos Exercícios
```python
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    def emprestar_livro(self, livro, usuario):
        if livro in self.livros:
            emprestimo = Emprestimo(livro, usuario)
            self.emprestimos.append(emprestimo)
            self.livros.remove(livro)
        else:
            print("Livro não disponível.")
    def devolver_livro(self, livro, usuario):
        for emp in self.emprestimos:
            if emp.livro == livro and emp.usuario == usuario:
                self.emprestimos.remove(emp)
                self.livros.append(livro)
                break

# Uso
biblio = Biblioteca()
livro1 = Livro("Python Básico", "Ana")
usuario1 = Usuario("Carlos")
biblio.adicionar_livro(livro1)
biblio.emprestar_livro(livro1, usuario1)
biblio.devolver_livro(livro1, usuario1)
```
