# Aula 08: Boas Práticas e Otimização

## 1. Explicações Conceituais

- **PEP8:** Guia de estilo para código Python.
- **Profiling:** Ferramentas para medir performance do código.
- **Otimização:** Técnicas para tornar o código mais eficiente.
- **Gerenciamento de dependências:** Uso de requirements.txt, pip, venv.

## 2. Práticas com Exemplos

### PEP8
- Use nomes descritivos para variáveis e funções.
- Indente com 4 espaços.
- Separe funções e classes com linhas em branco.

### Profiling
```python
import time

def funcao_lenta():
    time.sleep(1)

inicio = time.time()
funcao_lenta()
fim = time.time()
print(f'Tempo: {fim - inicio:.2f}s')
```

### Otimização de listas
```python
# Compreensão de listas é mais rápida que for tradicional
quadrados = [x**2 for x in range(10)]
```

### Gerenciamento de dependências
```bash
pip freeze > requirements.txt
python -m venv venv
```

## 3. Exercícios

1. Reescreva um código para seguir o PEP8.
2. Meça o tempo de execução de uma função que soma todos os números de 1 a 1.000.000.
3. Crie um ambiente virtual e instale o pacote requests.

## 4. Resolução dos Exercícios

### Exercício 1
```python
# Antes:
def soma(a,b):return a+b
# Depois:
def soma(a, b):
    return a + b
```

### Exercício 2
```python
import time

def soma():
    return sum(range(1, 1000001))

inicio = time.time()
soma()
fim = time.time()
print(f'Tempo: {fim - inicio:.2f}s')
```

### Exercício 3
```bash
python -m venv venv
venv\Scripts\activate
pip install requests
```
