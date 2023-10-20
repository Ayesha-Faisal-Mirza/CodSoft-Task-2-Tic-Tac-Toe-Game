import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [" " for _ in range(9)]
        self.buttons = []

        for i in range(9):
            button = tk.Button(root, text=" ", font=("Helvetica", 24), width=3, height=1,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.game_over = False
        self.current_player = "X"

    def initialize_game(self):
        self.board = [" " for _ in range(9)]
        self.update_ui()
        self.game_over = False
        self.current_player = "X"

    def make_move(self, index):
        if not self.game_over and self.board[index] == " ":
            self.board[index] = self.current_player
            self.update_ui()
            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
                return
            elif " " not in self.board:
                self.display_draw()
                return
            self.current_player = "O" if self.current_player == "X" else "X"
            self.root.title(f"Tic-Tac-Toe - Player's turn: {self.current_player}")

            if self.current_player == "O":
                ai_move = self.make_ai_move()
                self.make_move(ai_move)

    def make_ai_move(self):
        # Call minimax with alpha-beta pruning to get the AI move
        _, ai_move = self.minimax(self.board, "O")
        return ai_move

    def update_ui(self):
        for i in range(9):
            self.buttons[i]["text"] = self.board[i]

    def check_winner(self):
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None

    def display_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.root.title(f"Tic-Tac-Toe - Player {winner} wins!")
        self.game_over = True

    def display_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.root.title("Tic-Tac-Toe - It's a draw!")
        self.game_over = True

    def minimax(self, board, player):
        # Check for terminal states
        winner = self.check_winner()
        if winner:
            return 1 if winner == "O" else -1, None
        elif " " not in board:
            return 0, None

        if player == "O":  # Maximizing player (AI)
            best_score = -float("inf")
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score, _ = self.minimax(board, "X")
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move
        else:  # Minimizing player (human)
            best_score = float("inf")
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score, _ = self.minimax(board, "O")
                    board[i] = " "
                    if score < best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
