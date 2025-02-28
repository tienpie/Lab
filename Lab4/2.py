# Phân cụm
# Nhóm các đồi tượng có đặc điểm tương đồng mà không cần gắn nhãn

# Sử dụng data Iris để phân cụm
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load dữ liệu Iris
iris = datasets.load_iris()

# Dữ liệu đặc trưng (4 đặc trưng)
X = iris.data  # các đặc trưng

# Nhãn của các mẫu (dùng để so sánh sau)
y = iris.target  # nhãn của các mẫu

# Áp dụng KMean với số cụm là 3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# (Tuỳ chọn) Dùng PCA để giảm chiều dữ liệu xuống 2D để trực quan hóa
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# (Tuỳ chọn) Dự đoán nhãn phân cụm
labels = kmeans.predict(X)

# (Tuỳ chọn) In kết quả hoặc trực quan hóa
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.title('Phân cụm dữ liệu Iris bằng KMeans')
plt.xlabel('Thành phần chính 1')
plt.ylabel('Thành phần chính 2')
plt.colorbar(label='Nhãn phân cụm')
plt.show()