# Aula 05 — Trabalhando com Dados de Diferentes Fontes

## Objetivos
- Aprender a coletar dados de web, APIs e grandes volumes.

## Explicação Conceitual
Dados podem vir de diversas fontes: arquivos locais, web scraping, APIs e bancos de dados. Saber coletar e integrar esses dados é fundamental.

### Web Scraping
- Uso de requests e BeautifulSoup

### APIs
- Consumo de APIs REST com requests

### Grandes Volumes
- Leitura de arquivos grandes com chunks

## Prática com Exemplos
```python
import requests
from bs4 import BeautifulSoup

# Web scraping
url = 'https://example.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Consumo de API
api_url = 'https://api.exemplo.com/dados'
res = requests.get(api_url)
dados = res.json()

# Leitura de arquivos grandes
import pandas as pd
for chunk in pd.read_csv('arquivo_grande.csv', chunksize=10000):
    print(chunk.head())
```

## Exercícios
1. Faça um web scraping simples de uma página HTML.
2. Consuma uma API pública e carregue os dados em um DataFrame.

## Resolução dos Exercícios
```python
# Exercício 1
res = requests.get('https://example.com')
soup = BeautifulSoup(res.text, 'html.parser')

# Exercício 2
res = requests.get('https://api.publicapis.org/entries')
df = pd.DataFrame(res.json()['entries'])
```
