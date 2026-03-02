# Aula 10 — Módulos e Projeto Final

## Introdução Conceitual
Módulos são arquivos Python que agrupam funções, variáveis e classes. Permitem organizar o código e reutilizar funcionalidades. O projeto final integra os conceitos aprendidos.

## Prática Guiada
### 1. Importando Módulos
```python
import math
print(math.sqrt(16))

from random import randint
print(randint(1, 10))
```
### 2. Criando Módulos Próprios
Crie um arquivo `meu_modulo.py`:
```python
def saudacao():
    print("Olá do módulo!")
```
No arquivo principal:
```python
import meu_modulo
meu_modulo.saudacao()
```
### 3. Organização de Projeto
- Separe funções em arquivos diferentes conforme o tamanho do projeto.

## Exercício Proposto
- Desenvolva um jogo de adivinhação:
    - O programa gera um número aleatório entre 1 e 100.
    - O usuário tem 10 tentativas para adivinhar.
    - A cada tentativa, informe se o número é maior ou menor.
    - Ao final, exiba o número de tentativas utilizadas.
    - Registre as tentativas em uma lista.
    - Separe a lógica em funções.

## Resolução Comentada
```python
from random import randint

def jogar():
    numero_secreto = randint(1, 100)
    tentativas = []
    for i in range(10):
        palpite = int(input(f"Tentativa {i+1}/10: Digite um número: "))
        tentativas.append(palpite)
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {i+1} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")
    else:
        print(f"Não foi dessa vez! O número era {numero_secreto}.")
    print("Suas tentativas:", tentativas)

jogar()
```

## Dicas VSCode
- Use o terminal para rodar o projeto e testar módulos.

## Recursos
- [Módulos Python](https://docs.python.org/pt-br/3/tutorial/modules.html)
- [Biblioteca random](https://docs.python.org/pt-br/3/library/random.html)
