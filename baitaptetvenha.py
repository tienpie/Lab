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
