import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = np.random.rand(10, 10)  # Dữ liệu ma trận 10x10 ngẫu nhiên

plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap thể hiện sự phân bố của dữ liệu trên ma trận")
plt.show()