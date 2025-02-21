import matplotlib.pyplot as plt


Cty = ['A', 'B', 'C', 'D']
thiphan = [30, 25, 25, 20]
color = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Sửa lỗi danh sách màu

plt.figure(figsize=(6, 6))
plt.pie(thiphan, labels=Cty, colors=color, autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title("Biểu đồ tròn biểu hiện tỉ lệ thị phần của 4 công ty")
plt.show()
