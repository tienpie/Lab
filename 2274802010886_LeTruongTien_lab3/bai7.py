import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Biểu đồ phân tán
x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 300  # Kích thước điểm
colors = np.random.rand(100)       # Màu sắc ngẫu nhiên

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
plt.colorbar(label='Giá trị màu')
plt.title("Biểu đồ phân tán của hai biến ngẫu nhiên")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
