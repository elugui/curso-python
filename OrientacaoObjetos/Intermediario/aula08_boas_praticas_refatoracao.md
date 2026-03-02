# Aula 08: Boas Práticas e Refatoração

## Objetivos
- Identificar e aplicar boas práticas em orientação a objetos.
- Refatorar código para melhorar legibilidade e manutenção.

## Explicação Conceitual
### Boas Práticas
- Nomeação clara de classes, métodos e atributos.
- Princípio da responsabilidade única.
- Evitar código duplicado.
- Utilizar herança e composição de forma adequada.

### Refatoração
Refatorar é melhorar o código sem alterar seu comportamento externo, tornando-o mais limpo e eficiente.

## Prática com Exemplos
```python
# Código antes da refatoração
class Calculadora:
    def soma(self, a, b):
        return a + b
    def subtrai(self, a, b):
        return a - b
    def multiplica(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return 'Erro: divisão por zero'

# Após refatoração
class Calculadora:
    def __init__(self):
        self.operacoes = {
            'soma': lambda a, b: a + b,
            'subtrai': lambda a, b: a - b,
            'multiplica': lambda a, b: a * b,
            'divide': lambda a, b: a / b if b != 0 else 'Erro: divisão por zero'
        }
    def calcular(self, operacao, a, b):
        return self.operacoes[operacao](a, b)
```

## Exercícios
1. Identifique problemas de design em uma classe que faz tudo (exemplo: classe `Loja` que gerencia produtos, vendas e funcionários).
2. Refatore a classe para aplicar o princípio da responsabilidade única.

## Resolução dos Exercícios
```python
# Antes
class Loja:
    def __init__(self):
        self.produtos = []
        self.funcionarios = []
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    def vender(self, produto):
        print(f"Vendendo {produto}")

# Depois
class GerenciadorProdutos:
    def __init__(self):
        self.produtos = []
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

class GerenciadorFuncionarios:
    def __init__(self):
        self.funcionarios = []
    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

class Loja:
    def __init__(self):
        self.gerenciador_produtos = GerenciadorProdutos()
        self.gerenciador_funcionarios = GerenciadorFuncionarios()
    def vender(self, produto):
        print(f"Vendendo {produto}")
```
