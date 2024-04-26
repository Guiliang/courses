import tkinter as tk
import random


class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.geometry("800x800")
        self.resizable(False, False)

        self.width = 800
        self.height = 800
        self.cell_size = 20
        self.snake_direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]

        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(fill="both", expand=True)

        self.game_frame = tk.Frame(self)
        self.canvas = tk.Canvas(self.game_frame, bg='black', width=self.width, height=self.height)
        self.start_game()

    def start_game(self):
        self.menu_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.canvas.pack()
        self.setup_ui()
        self.run_game()

    def setup_ui(self):
        self.update_ui()
        self.bind("<KeyPress>", self.change_direction)

    def update_ui(self):
        self.canvas.delete('all')
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='green')

    def run_game(self):
        self.move_snake()
        self.after(100, self.run_game)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_direction == 'Left':
            head_x -= self.cell_size
        elif self.snake_direction == 'Right':
            head_x += self.cell_size
        elif self.snake_direction == 'Up':
            head_y -= self.cell_size
        elif self.snake_direction == 'Down':
            head_y += self.cell_size

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

        self.update_ui()

    def change_direction(self, event):
        opposite_directions = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
        if event.keysym in ['Left', 'Right', 'Up', 'Down']:
            # Check if the new direction is opposite to the current direction
            if event.keysym != opposite_directions[self.snake_direction]:
                self.snake_direction = event.keysym


if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
