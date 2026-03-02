# Aula 06: Produção e Deploy de Modelos

## Explicação Conceitual
- O que é deploy de modelos: transformar modelos em serviços utilizáveis.
- Pipeline de produção: versionamento, testes, automação.
- Ferramentas: Flask, FastAPI, Docker.
- Monitoramento e manutenção de modelos em produção.

## Prática com Exemplos
```python
# Exemplo de API com Flask
from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # modelo = pickle.load(open('modelo.pkl', 'rb'))
    # pred = modelo.predict([data['features']])
    pred = [0]  # Exemplo
    return jsonify({'prediction': pred[0]})

# Para rodar: app.run(debug=True)

# Exemplo de Dockerfile
# FROM python:3.9
# COPY . /app
# WORKDIR /app
# RUN pip install flask
# CMD ["python", "app.py"]
```

## Exercícios
1. Crie uma API simples para servir um modelo de ML.
2. Escreva um Dockerfile para empacotar a aplicação.
3. Explique a importância do monitoramento de modelos em produção.

## Resolução dos Exercícios
```python
# 1. API já demonstrada acima.
# 2. Dockerfile já demonstrado acima.
# 3. Monitoramento: garante que o modelo continue performando bem, detecta drift e problemas em tempo real.
```
