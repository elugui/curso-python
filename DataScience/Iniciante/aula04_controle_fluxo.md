# Aula 04 — Controle de Fluxo

## Explicação Conceitual
- Estruturas condicionais: if, elif, else.
- Laços de repetição: for, while.
- Funções: definição, parâmetros, retorno.

## Prática com Exemplos
```python
# Condicional
idade = 20
if idade >= 18:
    print("Adulto")
else:
    print("Menor de idade")

# Laço for
for i in range(5):
    print(i)

# Função
def saudacao(nome):
    return f"Olá, {nome}!"
```

## Exercícios
1. Escreva um código que imprime os números de 1 a 10 usando um laço.
2. Crie uma função que recebe dois números e retorna a soma.
3. Escreva um código que verifica se um número é par ou ímpar.

## Resolução dos Exercícios
```python
# Exercício 1
for i in range(1, 11):
    print(i)

# Exercício 2
def soma(a, b):
    return a + b

# Exercício 3
numero = 7
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```
