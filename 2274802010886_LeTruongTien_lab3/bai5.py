import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
labels = ["Q1", "Q2", "Q3", "Q4"]
A = [500, 700, 800, 600]
B = [450, 350, 650, 750]
C = [500, 250, 850, 600]

x = np.arange(len(labels))  # vị trí trên trục x
width = 0.25  # Độ rộng của mỗi cột

# Vẽ biểu đồ
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, A, width, label='A')
rects2 = ax.bar(x, B, width, label='B')
rects3 = ax.bar(x + width, C, width, label='C')

# Định dạng biểu đồ
ax.set_xlabel('Quý')
ax.set_ylabel('Doanh thu')
ax.set_title('Biểu đồ thanh nhóm thể hiện doanh thu của A, B, C trong 4 quý')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
