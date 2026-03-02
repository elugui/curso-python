# Aula 04 – Métodos Especiais e Construtores

## Explicação Conceitual
O método __init__ é o construtor da classe, chamado ao criar um objeto. Métodos especiais como __str__ e __repr__ personalizam a representação do objeto.

## Prática com Exemplos
```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

livro = Livro("Python Básico", "Ana Souza")
print(livro)  # Python Básico por Ana Souza
```

## Exercícios
1. Crie uma classe "Carro" com atributos marca e modelo, e personalize a exibição usando __str__.

## Resolução dos Exercícios
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

carro = Carro("Fiat", "Uno")
print(carro)  # Fiat Uno
```