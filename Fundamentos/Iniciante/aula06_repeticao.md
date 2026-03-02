# Aula 06 — Estruturas de Repetição

## Introdução Conceitual
Estruturas de repetição permitem executar um bloco de código várias vezes. Em Python, usamos `for` e `while` para criar laços.

## Prática Guiada
### 1. Laço for
```python
for i in range(5):
    print(i)
```
### 2. Laço while
```python
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
```
### 3. Comandos break, continue, pass
```python
for i in range(10):
    if i == 5:
        break  # Interrompe o laço
    if i % 2 == 0:
        continue  # Pula para o próximo
    print(i)
```

## Exercício Proposto
1. Gerar a tabuada de um número digitado pelo usuário usando for.
2. Criar um contador regressivo de 10 a 1 usando while.

## Resolução Comentada
```python
# Tabuada
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Contador regressivo
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
```

## Dicas VSCode
- Use o terminal para testar laços rapidamente.

## Recursos
- [Laços for e while](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements)
