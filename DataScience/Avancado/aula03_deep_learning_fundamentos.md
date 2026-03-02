# Aula 03: Deep Learning – Fundamentos

## Explicação Conceitual
- O que é deep learning: redes neurais profundas, aplicações e vantagens.
- Arquiteturas: MLP (perceptron multicamadas), CNN (convolucionais), RNN (recorrentes).
- Frameworks populares: TensorFlow, PyTorch.

## Prática com Exemplos
```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Exemplo de MLP para classificação
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(20,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(X_train, y_train, epochs=10)  # X_train: shape (n amostras, 20)

# Exemplo de CNN para imagens
cnn = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])
cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# cnn.fit(X_train, y_train, epochs=5)  # X_train: shape (n amostras, 28, 28, 1)
```

## Exercícios
1. Implemente uma MLP simples para classificação de dados tabulares.
2. Crie uma CNN para classificação de imagens.
3. Explique as diferenças entre MLP, CNN e RNN.

## Resolução dos Exercícios
```python
# 1. MLP
model = models.Sequential([
    layers.Dense(32, activation='relu', input_shape=(10,)),
    layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 2. CNN
cnn = models.Sequential([
    layers.Conv2D(16, (3,3), activation='relu', input_shape=(32,32,1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])
cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 3. MLP: dados tabulares; CNN: imagens; RNN: sequências temporais.
```
