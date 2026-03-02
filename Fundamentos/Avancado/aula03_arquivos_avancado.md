# Aula 03: Manipulação Avançada de Arquivos

## 1. Explicações Conceituais

- **Arquivos binários:** Manipulação de dados não textuais (imagens, áudio, etc).
- **Serialização:** Transformar objetos Python em formatos para armazenamento/transmissão (pickle, json).
- **Arquivos grandes:** Técnicas para ler e processar arquivos sem sobrecarregar a memória.

## 2. Práticas com Exemplos

### Leitura e escrita de arquivos binários
```python
with open('imagem.png', 'rb') as f:
    dados = f.read()

with open('copia.png', 'wb') as f:
    f.write(dados)
```

### Serialização com pickle
```python
import pickle

dados = {'nome': 'Python', 'ano': 1991}
with open('dados.pkl', 'wb') as f:
    pickle.dump(dados, f)

with open('dados.pkl', 'rb') as f:
    dados_carregados = pickle.load(f)
```

### Serialização com json
```python
import json

dados = {'nome': 'Python', 'ano': 1991}
with open('dados.json', 'w') as f:
    json.dump(dados, f)

with open('dados.json', 'r') as f:
    dados_carregados = json.load(f)
```

### Leitura eficiente de arquivos grandes
```python
with open('grande.txt') as f:
    for linha in f:
        processar(linha)
```

## 3. Exercícios

1. Escreva um programa que copie um arquivo binário.
2. Salve e recupere um dicionário usando pickle.
3. Salve e recupere um dicionário usando json.
4. Leia um arquivo texto grande linha a linha e conte o número de linhas.

## 4. Resolução dos Exercícios

### Exercício 1
```python
with open('origem.bin', 'rb') as f1, open('destino.bin', 'wb') as f2:
    f2.write(f1.read())
```

### Exercício 2
```python
import pickle

d = {'a': 1}
with open('d.pkl', 'wb') as f:
    pickle.dump(d, f)
with open('d.pkl', 'rb') as f:
    d2 = pickle.load(f)
```

### Exercício 3
```python
import json

d = {'a': 1}
with open('d.json', 'w') as f:
    json.dump(d, f)
with open('d.json', 'r') as f:
    d2 = json.load(f)
```

### Exercício 4
```python
contador = 0
with open('grande.txt') as f:
    for _ in f:
        contador += 1
print(contador)
```
