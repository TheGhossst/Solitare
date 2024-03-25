import tkinter as tk

class SolitaireGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Solitaire")
        
        self.card_width = 71
        self.card_height = 96

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg='green')
        self.canvas.pack()

        self.draw_board()
        self.setup_game()
        
    def draw_board(self):
        for i in range(7):
            x = 20 + i * 100
            y = 20
            self.canvas.create_rectangle(x, y, x + self.card_width, y + self.card_height, outline='black', fill='white')

    def setup_game(self):
        pass

def main():
    root = tk.Tk()
    solitaire_gui = SolitaireGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
