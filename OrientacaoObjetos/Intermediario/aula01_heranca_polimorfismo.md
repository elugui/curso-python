# Aula 01: Herança e Polimorfismo

## Objetivos
- Compreender os conceitos de herança e polimorfismo em Python.
- Aplicar herança para reutilização de código.
- Utilizar polimorfismo para flexibilidade de código.

## Explicação Conceitual
### Herança
Herança permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse), promovendo reutilização e organização do código.

### Polimorfismo
Polimorfismo permite que diferentes classes implementem métodos com o mesmo nome, mas comportamentos distintos, facilitando a extensão e manutenção do código.

## Prática com Exemplos
```python
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.falar())
```

## Exercícios
1. Crie uma classe `Veiculo` e duas subclasses `Carro` e `Moto`, cada uma com um método `mover` que imprime uma mensagem diferente.
2. Implemente um método polimórfico em ambas as subclasses.

## Resolução dos Exercícios
```python
class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo sobre quatro rodas.")

class Moto(Veiculo):
    def mover(self):
        print("A moto está se movendo sobre duas rodas.")

veiculos = [Carro(), Moto()]
for veiculo in veiculos:
    veiculo.mover()
```
