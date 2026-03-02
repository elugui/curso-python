# Aula 05 — Estruturas de Controle: Condicionais

## Introdução Conceitual
Condicionais permitem que o programa tome decisões com base em condições. Em Python, usamos `if`, `elif` e `else` para controlar o fluxo de execução.

## Prática Guiada
### 1. Estrutura Básica
```python
nota = 7
if nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
```
### 2. Condições Compostas
```python
idade = 18
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
```
### 3. Operador Ternário
```python
x = 10
y = 20
maior = x if x > y else y
print(maior)
```

## Exercício Proposto
1. Ler a nota de um aluno e exibir se foi aprovado (>=6), em recuperação (>=4 e <6) ou reprovado (<4).

## Resolução Comentada
```python
nota = float(input("Digite a nota do aluno: "))
if nota >= 6:
    print("Aprovado!")
elif nota >= 4:
    print("Em recuperação!")
else:
    print("Reprovado!")
```

## Dicas VSCode
- Use a identação correta (4 espaços) para blocos de código.

## Recursos
- [Estruturas condicionais](https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements)
