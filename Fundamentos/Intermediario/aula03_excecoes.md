# Aula 3: Tratamento de Exceções

## Introdução Conceitual
Exceções são erros detectados durante a execução do programa. O tratamento de exceções permite lidar com esses erros de forma controlada, evitando que o programa pare inesperadamente.

- **try/except**: captura exceções.
- **else**: executa se não houver exceção.
- **finally**: executa sempre, ocorrendo erro ou não.
- **raise**: lança uma exceção manualmente.

## Exemplos Práticos
### Tratando Erros de Entrada
```python
try:
    numero = int(input('Digite um número: '))
    print(f"Você digitou: {numero}")
except ValueError:
    print("Valor inválido! Digite um número inteiro.")
```

### Exceção Personalizada
```python
class ErroPersonalizado(Exception):
    pass

def dividir(a, b):
    if b == 0:
        raise ErroPersonalizado('Divisão por zero não permitida!')
    return a / b
```

## Exercícios Propostos
1. Implemente um programa que peça dois números e trate divisões por zero.
2. Crie uma função que só aceite strings como parâmetro e lance uma exceção caso contrário.

## Resolução dos Exercícios
### 1. Tratando divisão por zero
```python
try:
    a = float(input('Numerador: '))
    b = float(input('Denominador: '))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: divisão por zero!")
```

### 2. Função com tipo restrito
```python
def aceita_string(valor):
    if not isinstance(valor, str):
        raise TypeError('Apenas strings são aceitas!')
    print(f"String recebida: {valor}")

aceita_string('Python')
# aceita_string(123)  # Gera exceção
```

## Boas Práticas
- Capture exceções específicas.
- Forneça mensagens de erro claras.
- Use exceções personalizadas para regras de negócio.