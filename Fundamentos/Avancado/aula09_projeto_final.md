# Aula 09: Projeto Final

## 1. Explicações Conceituais

- **Projeto integrador:** Aplicação dos conceitos aprendidos em um projeto prático.
- **Planejamento:** Definição de escopo, funcionalidades e etapas.
- **Desenvolvimento:** Implementação incremental, testes e documentação.

## 2. Proposta de Projeto

Desenvolva uma aplicação Python que consuma uma API pública, armazene dados em arquivo e ofereça uma interface simples (CLI ou web).

### Sugestão de etapas:
1. Escolha uma API pública (ex: https://jsonplaceholder.typicode.com/)
2. Consuma dados da API usando requests
3. Armazene os dados em arquivo (json ou csv)
4. Implemente uma interface para consultar os dados
5. Adicione testes automatizados
6. Documente o projeto

## 3. Exercícios

1. Planeje o escopo do seu projeto.
2. Implemente a coleta e armazenamento dos dados.
3. Crie a interface de consulta.
4. Escreva testes para as funções principais.
5. Documente o uso do projeto.

## 4. Resolução dos Exercícios (Exemplo)

### Exercício 1
- Definir funcionalidades: buscar posts, salvar em arquivo, consultar por título.

### Exercício 2
```python
import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts')
with open('posts.json', 'w') as f:
    json.dump(r.json(), f)
```

### Exercício 3
```python
def buscar_por_titulo(titulo):
    with open('posts.json') as f:
        posts = json.load(f)
    return [p for p in posts if titulo.lower() in p['title'].lower()]
```

### Exercício 4
```python
def test_buscar_por_titulo():
    resultado = buscar_por_titulo('qui')
    assert isinstance(resultado, list)
```

### Exercício 5
- Escreva um README explicando como rodar o projeto e exemplos de uso.
