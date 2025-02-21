import matplotlib.pyplot as plt
import numpy as np

t =np.linspace(0, 10, 100)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.sin(t) * np.cos(t)

#tao bieu do cac duong theo thoi gian
plt.figure(figsize=(12,6))
plt.plot(t, y1, label="sin(t)", linestyle="-", color="b")
plt.plot(t, y2, label="cos(t)", linestyle="--", color="r")
plt.plot(t, y3, label="sin(t) * cos(t)", linestyle="-.", color="g")
plt.title("Biểu đồ các hàm theo thời gian")
plt.xlabel("Thời gian (t)")
plt.ylabel("Giá trị")
plt.legend()  
plt.grid(True)  
plt.show() 
