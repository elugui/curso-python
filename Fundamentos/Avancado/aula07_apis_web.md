# Aula 07: Integração com APIs e Web

## 1. Explicações Conceituais

- **APIs REST:** Interfaces para comunicação entre sistemas via HTTP.
- **Requests:** Biblioteca para consumir APIs em Python.
- **FastAPI/Flask:** Frameworks para criar APIs web.

## 2. Práticas com Exemplos

### Consumo de API com requests
```python
import requests

resposta = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(resposta.json())
```

### Criando uma API simples com Flask
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({'mensagem': 'Olá, API!'})

if __name__ == '__main__':
    app.run(debug=True)
```

## 3. Exercícios

1. Consuma uma API pública e exiba o resultado.
2. Crie uma rota Flask que retorna um dicionário em formato JSON.
3. Modifique a rota para receber um parâmetro e retornar uma mensagem personalizada.

## 4. Resolução dos Exercícios

### Exercício 1
```python
import requests

r = requests.get('https://api.github.com')
print(r.json())
```

### Exercício 2
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dados')
def dados():
    return jsonify({'nome': 'Python'})
```

### Exercício 3
```python
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return jsonify({'mensagem': f'Olá, {nome}!'})
```
