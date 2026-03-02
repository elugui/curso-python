# Aula 2: Manipulação de Arquivos

## Introdução Conceitual
Manipular arquivos é essencial para ler e gravar dados de forma persistente. Python oferece funções simples para abrir, ler, escrever e fechar arquivos.

- **open()**: abre um arquivo.
- **read() / readline() / readlines()**: lê o conteúdo.
- **write()**: escreve no arquivo.
- **with**: garante o fechamento automático do arquivo.

## Exemplos Práticos
### Leitura de Arquivo
```python
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### Escrita em Arquivo
```python
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Olá, Python!')
```

### Usando pathlib
```python
from pathlib import Path
p = Path('dados.txt')
print(p.read_text())
```

## Exercícios Propostos
1. Leia um arquivo texto e conte o número de linhas.
2. Escreva uma lista de nomes em um novo arquivo, um por linha.

## Resolução dos Exercícios
### 1. Contar linhas
```python
with open('dados.txt', 'r') as f:
    linhas = f.readlines()
    print(f"Total de linhas: {len(linhas)}")
```

### 2. Escrever nomes
```python
nomes = ['Ana', 'Bruno', 'Carlos']
with open('nomes.txt', 'w') as f:
    for nome in nomes:
        f.write(nome + '\n')
```

## Boas Práticas
- Sempre use `with` para manipular arquivos.
- Trate exceções ao lidar com arquivos inexistentes.
- Prefira pathlib para caminhos portáveis.