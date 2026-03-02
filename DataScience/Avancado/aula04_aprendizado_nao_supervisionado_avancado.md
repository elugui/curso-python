# Aula 04: Aprendizado Não Supervisionado Avançado

## Explicação Conceitual
- Modelos de clustering avançados: DBSCAN, Gaussian Mixture Models (GMM).
- Técnicas de redução de dimensionalidade: t-SNE, UMAP.
- Aplicações práticas: segmentação, visualização de dados complexos.

## Prática com Exemplos
```python
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# DBSCAN
X, _ = make_moons(n_samples=200, noise=0.05)
dbscan = DBSCAN(eps=0.2).fit(X)
plt.scatter(X[:,0], X[:,1], c=dbscan.labels_)
plt.title('DBSCAN')
plt.show()

# Gaussian Mixture
gmm = GaussianMixture(n_components=2).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:,0], X[:,1], c=labels)
plt.title('GMM')
plt.show()

# t-SNE
from sklearn.datasets import load_digits
digits = load_digits()
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(digits.data)
plt.scatter(X_tsne[:,0], X_tsne[:,1], c=digits.target)
plt.title('t-SNE')
plt.show()
```

## Exercícios
1. Aplique DBSCAN em um conjunto de dados não linear.
2. Use GMM para clusterizar dados e compare com K-means.
3. Utilize t-SNE ou UMAP para visualizar dados de alta dimensão.

## Resolução dos Exercícios
```python
# 1. DBSCAN
X, _ = make_moons(n_samples=100, noise=0.1)
db = DBSCAN(eps=0.3).fit(X)
print(db.labels_)

# 2. GMM vs K-means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(X)
gmm = GaussianMixture(n_components=2).fit(X)
print('K-means:', kmeans.labels_)
print('GMM:', gmm.predict(X))

# 3. t-SNE
from sklearn.datasets import load_iris
iris = load_iris()
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(iris.data)
print(X_tsne[:5])
```
