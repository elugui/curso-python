# Aula 02 — Variáveis e Tipos de Dados

## Introdução Conceitual
Variáveis são espaços na memória para armazenar dados. Em Python, não é necessário declarar o tipo da variável, pois a linguagem é de tipagem dinâmica. Os principais tipos primitivos são: inteiro (`int`), ponto flutuante (`float`), texto (`str`) e booleano (`bool`).

## Prática Guiada
### 1. Declarando Variáveis
```python
idade = 25
altura = 1.75
nome = "Ana"
estudante = True
```
### 2. Verificando Tipos
```python
print(type(idade))  # <class 'int'>
print(type(altura)) # <class 'float'>
```
### 3. Conversão de Tipos
```python
idade_str = str(idade)
altura_int = int(altura)
```

## Exercício Proposto
1. Crie variáveis para nome, idade, altura e estudante.
2. Exiba os valores e seus tipos.
3. Converta a idade para string e a altura para inteiro.

## Resolução Comentada
```python
nome = "Ana"
idade = 25
altura = 1.75
estudante = True

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(estudante, type(estudante))

idade_str = str(idade)
altura_int = int(altura)
print(idade_str, type(idade_str))
print(altura_int, type(altura_int))
```

## Dicas VSCode
- Use o atalho Ctrl+` para abrir o terminal.
- Utilize a extensão Python para realce de sintaxe.

## Recursos
- [Tipos de dados Python](https://docs.python.org/pt-br/3/library/stdtypes.html)
