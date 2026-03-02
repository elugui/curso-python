# Aula 08 — Listas

## Introdução Conceitual
Listas são coleções ordenadas e mutáveis de elementos. Permitem armazenar vários valores em uma única variável.

## Prática Guiada
### 1. Criando e Acessando Listas
```python
numeros = [1, 2, 3, 4]
print(numeros[0])  # 1
print(numeros[-1]) # 4
```
### 2. Métodos de Lista
```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
frutas.remove("banana")
frutas.insert(1, "uva")
print(frutas)
```
### 3. Iterando sobre Listas
```python
for fruta in frutas:
    print(fruta)
```
### 4. Funções Úteis
```python
print(len(frutas))
print(min(numeros))
print(max(numeros))
print(sum(numeros))
```

## Exercício Proposto
1. Criar uma lista de compras, adicionar e remover itens, exibir todos os itens e o total.

## Resolução Comentada
```python
compras = []
while True:
    item = input("Adicione um item (ou 'sair'): ")
    if item == 'sair':
        break
    compras.append(item)
print("Itens:", compras)
print("Total:", len(compras))
```

## Dicas VSCode
- Use a função de autocompletar para explorar métodos de lista.

## Recursos
- [Listas Python](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
