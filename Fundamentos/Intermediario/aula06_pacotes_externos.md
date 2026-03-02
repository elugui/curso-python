# Aula 6: Instalação e Uso de Pacotes Externos

## Introdução Conceitual
Pacotes externos ampliam as funcionalidades do Python. O `pip` é o gerenciador padrão para instalar e atualizar pacotes.
- **pip**: instala, remove e atualiza pacotes.
- **venv**: cria ambientes virtuais isolados.
- **import**: importa módulos e pacotes para uso no código.

## Exemplos Práticos
### Instalando um Pacote
```bash
pip install requests
```

### Usando o requests
```python
import requests
resposta = requests.get('https://api.github.com')
print(resposta.status_code)
```

### Trabalhando com JSON
```python
import json
dados = {'nome': 'Ana', 'idade': 22}
texto = json.dumps(dados)
print(texto)
```

## Exercícios Propostos
1. Instale o pacote `requests` e faça uma requisição para https://api.github.com.
2. Leia um arquivo JSON e exiba os dados em formato de dicionário.

## Resolução dos Exercícios
### 1. Requisição HTTP
```python
import requests
r = requests.get('https://api.github.com')
print(r.status_code)
```

### 2. Ler arquivo JSON
```python
import json
with open('dados.json', 'r') as f:
    dados = json.load(f)
print(dados)
```

## Boas Práticas
- Use ambientes virtuais para cada projeto.
- Liste dependências em requirements.txt.
- Consulte a documentação dos pacotes para exemplos de uso.