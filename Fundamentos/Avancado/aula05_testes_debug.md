# Aula 05: Testes e Depuração

## 1. Explicações Conceituais

- **Testes unitários:** Garantem que partes do código funcionam como esperado.
- **Frameworks de teste:** `unittest` (nativo), `pytest` (popular).
- **Mocking:** Simulação de objetos para isolar testes.
- **Depuração:** Técnicas para encontrar e corrigir bugs.

## 2. Práticas com Exemplos

### Teste com unittest
```python
import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

### Teste com pytest
```python
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
```

### Mocking
```python
from unittest.mock import Mock

obj = Mock()
obj.metodo.return_value = 10
print(obj.metodo())
```

### Depuração com breakpoint
```python
def soma(a, b):
    breakpoint()
    return a + b

soma(2, 3)
```

## 3. Exercícios

1. Escreva um teste unitário para uma função que verifica se um número é par.
2. Use mocking para simular uma chamada de API.
3. Use um breakpoint para depurar uma função que calcula o fatorial.

## 4. Resolução dos Exercícios

### Exercício 1
```python
import unittest

def eh_par(n):
    return n % 2 == 0

class TestPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(5))
```

### Exercício 2
```python
from unittest.mock import Mock

api = Mock()
api.get_dados.return_value = {'status': 'ok'}
print(api.get_dados())
```

### Exercício 3
```python
def fatorial(n):
    breakpoint()
    if n == 0:
        return 1
    return n * fatorial(n-1)

fatorial(5)
```
