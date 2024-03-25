import tkinter as tk

class SolitaireGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Solitaire")

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg='green')
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        pass


def main():
    root = tk.Tk()
    solitaire_gui = SolitaireGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
