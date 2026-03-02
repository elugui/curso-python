# Aula 09 – Projeto Prático

## Proposta de Projeto Integrador
Desenvolva um sistema completo aplicando os conceitos aprendidos: herança, polimorfismo, composição, encapsulamento, métodos especiais, UML, boas práticas e padrões de projeto.

### Sugestão de Projeto
Sistema de gerenciamento de biblioteca:
- Cadastro de livros, autores e usuários
- Empréstimo e devolução de livros
- Relatórios

## Orientação e Acompanhamento
- Divida o projeto em etapas
- Oriente sobre modelagem UML antes da implementação
- Sugira revisões de código e refatoração

## Exercício
Implemente o sistema proposto, documentando cada etapa e justificando as escolhas de design.

## Resolução (Exemplo de Estrutura)
```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Autor:
    def __init__(self, nome):
        self.nome = nome

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
```
