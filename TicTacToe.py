import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master

        self.master.title("Tic Tac Toe")
        self.master.geometry("400x450")
        self.master.config(bg= "#303030")

        self.color1 = "#2196f3" # Blue
        self.color2 = "#f44336" # Red
        self.color3 = "black"
        self.color4 = "white"

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.x_wins = 0
        self.o_wins = 0

        self.x_label = tk.Label(master, text=f"X Wins: {self.x_wins}", font=("Helvetica", 12), bg="#303030", fg=self.color1)
        self.x_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.o_label = tk.Label(master, text=f"O Wins: {self.o_wins}", font=("Helvetica", 12), bg="#303030", fg=self.color2)
        self.o_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", width=8, height=3,
                                   font=("Helvetica", 18), bg=self.color3, fg=self.color4,
                                   activebackground=self.color3, activeforeground=self.color1,
                                   command=lambda i=i, j=j: self.click_button(i, j))
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        self.reset_button = tk.Button(master, text="Reset", font=("Helvetica", 12),bg=self.color3, fg=self.color4,
                                      activebackground= self.color3, activeforeground=self.color4, command=self.reset_game)
        self.reset_button.grid(row=3, column=1, pady=10)

    def click_button(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg=self.color2 if self.current_player == "O" else self.color1)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Victory!", f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.x_wins += 1
                    self.x_label.config(text=f"X Wins: {self.x_wins}")
                else:
                    self.o_wins += 1
                    self.o_label.config(text=f"O Wins: {self.o_wins}")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "The game ended in a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", fg=self.color4)

root = tk.Tk()
app = TicTacToe(root)
root.mainloop()