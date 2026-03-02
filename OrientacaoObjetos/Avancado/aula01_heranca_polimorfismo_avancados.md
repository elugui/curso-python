# Aula 01 – Herança e Polimorfismo Avançados

## Explicação Conceitual
- Revisão de herança simples e múltipla
- Polimorfismo em profundidade
- Superclasse e sobrescrita de métodos
- Princípios SOLID relacionados

### Herança
Explique o conceito de herança, diferença entre simples e múltipla, exemplos práticos.

### Polimorfismo
Demonstre polimorfismo com exemplos de sobrescrita de métodos e uso de super().

### Princípios SOLID
Apresente os princípios SOLID relacionados à herança e polimorfismo (LSP, OCP).

## Prática com Exemplos
```python
class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

animais = [Cachorro(), Gato()]
for animal in animais:
    animal.falar()
```

## Exercícios
1. Crie uma classe base Veiculo e duas subclasses Carro e Moto, cada uma com um método mover().
2. Implemente polimorfismo para que cada veículo se mova de forma diferente.

## Resolução dos Exercícios
```python
class Veiculo:
    def mover(self):
        print("Veículo está se movendo.")

class Carro(Veiculo):
    def mover(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def mover(self):
        print("Moto está acelerando.")

veiculos = [Carro(), Moto()]
for v in veiculos:
    v.mover()
```
