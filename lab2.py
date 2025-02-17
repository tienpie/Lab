## BÀI TẬP' KÊT NUMPY
# Tạo một máng numpy có kích thươc 150 x 5. Hãy tưởng tượng mắng này chứa 150 mẫu về chiều cao, cần nặng, tuổi, lương, GPA của sinh viên VLU 
# Chia mảng bốn cột đầu tiên thành một biến có tên là X và cột cuối cùng thành y 
# Chia X thành X_tran và X_test chứa 70% dữ liệu và chia y thành y _train và y_test, trong đó y_train chứa 70% dữ liệu. 
# Tạo 10 tập dữ liệu không chòng chéo của _train 

# -*- coding: utf-8 -*-
import numpy as np
from sklearn.model_selection import train_test_split

# Đặt seed để kết quả nhất quán
np.random.seed(42)

# 1. Tạo một mảng NumPy có kích thước 150x5
data = np.random.uniform(0, 10, (150, 5))

# 2. Chia mảng thành X (4 cột đầu) và y (cột cuối)
X = data[:, :-1]  # Lấy tất cả hàng, bỏ cột cuối
y = data[:, -1]   # Lấy cột cuối cùng

# 3. Chia dữ liệu thành tập train (70%) và test (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Tạo 10 tập dữ liệu không chồng chéo từ X_train và y_train
num_splits = 10
split_size = len(X_train) // num_splits  # Kích thước mỗi tập con

X_splits = [X_train[i * split_size:(i + 1) * split_size] for i in range(num_splits)]
y_splits = [y_train[i * split_size:(i + 1) * split_size] for i in range(num_splits)]

# Kiểm tra kích thước các tập dữ liệu
print(f"Kích thước X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"Số lượng tập con: {len(X_splits)}, Kích thước mỗi tập: {X_splits[0].shape}")
########
# Bài tập tết về nhà

# Cho ma trận = [
#  [99,99,99],
#  [99,99,99],
#  [99,99,99]
#]
# giá sử 0 = 0 và 1 là x 
# nhận đầu vào từ phía X và 0 luân phiên 
# cho các bạn một cập chí số 
# nếu phía x nhập ((0,0)) thì ma trận trở thành
#[
#[X,99,99],
#[99,99,99],
#[99,99,99]
#]
# nếu phía O nhập ((0,0)) thì yêu câu nhập lại và nếu không thì điền vào ma trận
# thử thách của các bạn ở nhà ăn tết: nếu ai đó có ba ô liên tiếp thì dừng trò chơi.

# -*- coding: utf-8 -*-
import numpy as np

# Khởi tạo ma trận 3x3 với giá trị 99
board = np.full((3, 3), 99)

# Hiển thị bàn cờ
def print_board():
    symbols = {99: ' ', 0: 'O', 1: 'X'}
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * 9)

# Kiểm tra điều kiện thắng
def check_winner():
    for i in range(3):
        # Kiểm tra hàng và cột
        if (board[i, 0] == board[i, 1] == board[i, 2] != 99) or \
           (board[0, i] == board[1, i] == board[2, i] != 99):
            return True
        
    # Kiểm tra đường chéo
    if (board[0, 0] == board[1, 1] == board[2, 2] != 99) or \
       (board[0, 2] == board[1, 1] == board[2, 0] != 99):
        return True
    
    return False

# Chạy trò chơi
def play_game():
    turn = 1  # Bắt đầu với X (1)
    moves = 0
    print_board()
    
    while moves < 9:
        player = "X" if turn == 1 else "O"
        try:
            row, col = map(int, input(f"Người chơi {player}, nhập hàng và cột (0-2, cách nhau bởi dấu cách): ").split())
            if board[row, col] == 99:  # Vị trí trống
                board[row, col] = turn
                print_board()
                if check_winner():
                    print(f"🎉 Người chơi {player} thắng! 🎉")
                    return
                turn = 1 - turn  # Chuyển lượt
                moves += 1
            else:
                print("⚠️ Ô đã được chọn, hãy nhập lại!")
        except (ValueError, IndexError):
            print("⚠️ Vui lòng nhập hai số trong khoảng [0,2]!")

    print("⚖️ Trò chơi hòa!")

# Bắt đầu trò chơi
play_game()
