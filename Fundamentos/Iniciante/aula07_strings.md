# Aula 07 — Strings

## Introdução Conceitual
Strings são sequências de caracteres usadas para armazenar e manipular texto. Python oferece diversos métodos para trabalhar com strings.

## Prática Guiada
### 1. Indexação e Fatiamento
```python
texto = "Python"
print(texto[0])    # P
print(texto[-1])   # n
print(texto[1:4])  # yth
```
### 2. Métodos de String
```python
frase = "  Olá, Mundo!  "
print(frase.upper())      # "  OLÁ, MUNDO!  "
print(frase.lower())      # "  olá, mundo!  "
print(frase.strip())      # "Olá, Mundo!"
print(frase.replace("Mundo", "Python")) # "  Olá, Python!  "
print(frase.split(","))  # ['  Olá', ' Mundo!  ']
```
### 3. Verificações
```python
print("abc".isdigit())  # False
print("123".isdigit())  # True
print("abc".isalpha())  # True
```
### 4. Strings Multilinha
```python
texto = """Linha 1
Linha 2"""
print(texto)
```

## Exercício Proposto
1. Ler uma frase do usuário, contar o número de palavras, exibir a frase em maiúsculas e invertida.

## Resolução Comentada
```python
frase = input("Digite uma frase: ")
palavras = frase.split()
print("Número de palavras:", len(palavras))
print("Maiúsculas:", frase.upper())
print("Invertida:", frase[::-1])
```

## Dicas VSCode
- Use o recurso de busca (Ctrl+F) para encontrar métodos de string rapidamente.

## Recursos
- [Strings Python](https://docs.python.org/pt-br/3/library/stdtypes.html#text-sequence-type-str)
