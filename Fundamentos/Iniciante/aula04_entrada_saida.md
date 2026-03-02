# Aula 04 — Entrada e Saída de Dados

## Introdução Conceitual
Entrada e saída de dados são fundamentais para a interação com o usuário. Em Python, usamos `input()` para ler dados e `print()` para exibir informações.

## Prática Guiada
### 1. Lendo Dados do Usuário
```python
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
```
### 2. Exibindo Dados
```python
print("Olá,", nome)
print(f"Você tem {idade} anos.")
```
### 3. Formatação de Strings
```python
cidade = "São Paulo"
print("Bem-vindo a {}!".format(cidade))
print("Bem-vindo a", cidade)
```
### 4. Caracteres Especiais
```python
print("Linha 1\nLinha 2")
print("Coluna 1\tColuna 2")
```

## Exercício Proposto
1. Solicite nome, idade e cidade do usuário e exiba uma mensagem formatada de boas-vindas.

## Resolução Comentada
```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

print(f"Bem-vindo, {nome}! Você tem {idade} anos e mora em {cidade}.")
```

## Dicas VSCode
- Use f-strings para facilitar a formatação de mensagens.

## Recursos
- [Função input()](https://docs.python.org/pt-br/3/library/functions.html#input)
- [Função print()](https://docs.python.org/pt-br/3/library/functions.html#print)
