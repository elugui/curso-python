# Aula 07: Modelos Não Supervisionados

## Explicação Conceitual
- O que são modelos não supervisionados: definição e aplicações.
- Clustering: agrupamento de dados (K-means, Hierárquico).
- Redução de dimensionalidade: conceito e uso do PCA.
- Aplicações práticas: segmentação de clientes, compressão de dados.

## Prática com Exemplos
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Clustering com K-means
X, _ = make_blobs(n_samples=100, centers=3, n_features=2)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_
plt.scatter(X[:,0], X[:,1], c=labels)
plt.title('K-means Clustering')
plt.show()

# Redução de dimensionalidade com PCA
from sklearn.datasets import load_iris
iris = load_iris()
pca = PCA(n_components=2)
X_pca = pca.fit_transform(iris.data)
plt.scatter(X_pca[:,0], X_pca[:,1], c=iris.target)
plt.title('PCA - Iris')
plt.show()
```

## Exercícios
1. Aplique K-means em um conjunto de dados sintético e visualize os clusters.
2. Use PCA para reduzir a dimensionalidade de um dataset.
3. Cite aplicações práticas de clustering e PCA.

## Resolução dos Exercícios
```python
# 1. K-means
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=50, centers=2)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print('Labels:', kmeans.labels_)

# 2. PCA
from sklearn.datasets import load_wine
wine = load_wine()
pca = PCA(n_components=2)
X_pca = pca.fit_transform(wine.data)
print('Shape após PCA:', X_pca.shape)

# 3. Aplicações: segmentação de clientes, compressão de imagens, visualização de dados de alta dimensão.
```
