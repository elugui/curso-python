# Aula 06: Design Patterns em Python

## 1. Explicações Conceituais

- **Design Patterns:** Soluções reutilizáveis para problemas comuns de design de software.
- **Singleton:** Garante que uma classe tenha apenas uma instância.
- **Factory:** Cria objetos sem expor a lógica de criação.
- **Observer:** Permite que objetos sejam notificados sobre mudanças em outros objetos.

## 2. Práticas com Exemplos

### Singleton
```python
class Singleton:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```

### Factory
```python
class Carro:
    def dirigir(self):
        print('Dirigindo')

def fabrica(tipo):
    if tipo == 'carro':
        return Carro()

obj = fabrica('carro')
obj.dirigir()
```

### Observer
```python
class Observado:
    def __init__(self):
        self.observers = []
    def registrar(self, obs):
        self.observers.append(obs)
    def notificar(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observador:
    def update(self, msg):
        print(f'Notificado: {msg}')

obs = Observador()
obj = Observado()
obj.registrar(obs)
obj.notificar('Mudou!')
```

## 3. Exercícios

1. Implemente o padrão Singleton para uma classe de configuração.
2. Crie uma fábrica que retorna diferentes tipos de veículos.
3. Implemente o padrão Observer para um sistema de notificações.

## 4. Resolução dos Exercícios

### Exercício 1
```python
class Config:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```

### Exercício 2
```python
class Moto:
    def dirigir(self):
        print('Pilotando')

def fabrica(tipo):
    if tipo == 'carro':
        return Carro()
    elif tipo == 'moto':
        return Moto()

obj = fabrica('moto')
obj.dirigir()
```

### Exercício 3
```python
# Igual ao exemplo acima, adaptando para o contexto desejado.
```
