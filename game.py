import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and self.check_winner() is None:
            self.buttons[i][j]["text"] = self.current_player
            self.board[i][j] = self.current_player

            if self.check_winner():
                self.show_winner(self.current_player)
            elif self.check_draw():
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return None

    def check_draw(self):
        return all([cell != "" for row in self.board for cell in row])

    def show_winner(self, winner):
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
        self.reset_game()

    def show_draw(self):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
