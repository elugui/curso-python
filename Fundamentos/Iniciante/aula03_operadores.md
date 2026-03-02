# Aula 03 — Operadores

## Introdução Conceitual
Operadores são símbolos que realizam operações sobre valores e variáveis. Em Python, temos operadores aritméticos, relacionais, lógicos e de atribuição.

## Prática Guiada
### 1. Operadores Aritméticos
```python
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
```
### 2. Operadores Relacionais
```python
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a <= b)  # False
```
### 3. Operadores Lógicos
```python
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
```
### 4. Operadores de Atribuição
```python
c = 5
c += 2  # c = c + 2
print(c) # 7
```

## Exercício Proposto
1. Solicite dois números ao usuário e exiba o resultado das operações aritméticas entre eles.
2. Verifique se o primeiro número é maior que o segundo.

## Resolução Comentada
```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão:", num1 / num2)
print("Maior que?", num1 > num2)
```

## Dicas VSCode
- Use o terminal integrado para testar rapidamente operações.

## Recursos
- [Operadores Python](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex)
