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

        for i in range(4):
            x = 20 + (i + 2) * 100
            y = 20
            self.canvas.create_rectangle(x, y, x + self.card_width, y + self.card_height, outline='black', fill='white')
    
    def setup_game(self):
        self.cards = []
        for i in range(7):
            for j in range(i + 1):
                card = {'rank': 'blah', 'suit': 'Blah'}  
                self.cards.append(card)
                x = 20 + i * 100
                y = 20 + j * 20
                self.draw_card(card, x, y)
                
    def draw_card(self, card, x, y):
        rank = card['rank']
        suit = card['suit']
        self.canvas.create_rectangle(x, y, x + self.card_width, y + self.card_height, outline='black', fill='white')
        self.canvas.create_text(x + 10, y + 10, anchor='nw', text=rank, font=('Helvetica', '14'), fill='red')
        self.canvas.create_text(x + 10, y + 30, anchor='nw', text=suit, font=('Helvetica', '14'), fill='red')

def main():
    root = tk.Tk()
    solitaire_gui = SolitaireGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
