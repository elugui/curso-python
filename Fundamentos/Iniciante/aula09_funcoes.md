# Aula 09 — Funções

## Introdução Conceitual
Funções são blocos de código reutilizáveis que executam uma tarefa específica. Facilitam a organização, manutenção e reutilização do código.

## Prática Guiada
### 1. Definindo Funções
```python
def saudacao():
    print("Olá!")
saudacao()
```
### 2. Parâmetros e Argumentos
```python
def soma(a, b):
    return a + b
print(soma(2, 3))
```
### 3. Retorno de Valores
```python
def quadrado(x):
    return x ** 2
```
### 4. Parâmetros Padrão
```python
def mensagem(texto="Olá, mundo!"):
    print(texto)
mensagem()
mensagem("Oi!")
```
### 5. Escopo de Variáveis
```python
def func():
    local = 10
    print(local)
# print(local)  # Erro: variável local não existe fora da função
```

## Exercício Proposto
1. Criar funções para calcular área de formas geométricas (quadrado, retângulo, triângulo).
2. Criar uma função que verifica se um número é primo.

## Resolução Comentada
```python
def area_quadrado(lado):
    return lado * lado

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(area_quadrado(4))
print(area_retangulo(3, 5))
print(area_triangulo(6, 2))
print(eh_primo(7))
```

## Dicas VSCode
- Use docstrings para documentar funções.

## Recursos
- [Funções Python](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)
