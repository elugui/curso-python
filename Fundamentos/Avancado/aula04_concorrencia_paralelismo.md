# Aula 04: Programação Concorrente e Paralela

## 1. Explicações Conceituais

- **Concorrência vs Paralelismo:** Diferença entre executar tarefas "ao mesmo tempo" e realmente em paralelo.
- **Threads:** Execução concorrente dentro do mesmo processo.
- **Processos:** Execução paralela em processos separados.
- **Asyncio:** Programação assíncrona baseada em eventos.

## 2. Práticas com Exemplos

### Threads
```python
import threading

def tarefa():
    print('Executando em thread')

thread = threading.Thread(target=tarefa)
thread.start()
thread.join()
```

### Processos
```python
from multiprocessing import Process

def tarefa():
    print('Executando em processo')

p = Process(target=tarefa)
p.start()
p.join()
```

### Asyncio
```python
import asyncio

async def tarefa():
    print('Executando async')

asyncio.run(tarefa())
```

## 3. Exercícios

1. Crie um programa que execute duas funções simultaneamente usando threads.
2. Crie um programa que execute duas funções simultaneamente usando processos.
3. Implemente duas funções assíncronas e execute-as com asyncio.

## 4. Resolução dos Exercícios

### Exercício 1
```python
import threading

def f1():
    print('f1')
def f2():
    print('f2')

thread1 = threading.Thread(target=f1)
thread2 = threading.Thread(target=f2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
```

### Exercício 2
```python
from multiprocessing import Process

def f1():
    print('f1')
def f2():
    print('f2')

p1 = Process(target=f1)
p2 = Process(target=f2)
p1.start()
p2.start()
p1.join()
p2.join()
```

### Exercício 3
```python
import asyncio

async def f1():
    print('f1')
async def f2():
    print('f2')

async def main():
    await asyncio.gather(f1(), f2())

asyncio.run(main())
```
