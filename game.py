import tkinter as tk
import random

class SolitaireGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Solitaire")
        
        self.card_width = 71
        self.card_height = 96
        
        self.deck = self.generate_deck()
        self.stock_pile = []
        self.foundation_piles = [[] for _ in range(4)]
        self.tableau_piles = [[] for _ in range(7)]

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg='green')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_board()
        self.setup_game()
        
    def generate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck
        
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
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.pop(0)
                self.tableau_piles[i].append(card)
                x = 20 + i * 100
                y = 20 + j * 20
                self.draw_card(card, x, y)
        for pile_index in range(7):
            self.show_top_card('tableau', pile_index)
        
        for i in range(1, len(self.deck)):
            self.stock_pile.append(self.deck.pop(0))
        
        self.show_top_card('stock')
        self.show_top_card('foundation', 0)
        
    def show_top_card(self, pile_type, pile_index=None):
        if pile_type == 'tableau':
            pile = self.tableau_piles[pile_index]
        elif pile_type == 'foundation':
            pile = self.foundation_piles[pile_index]
        elif pile_type == 'stock':
            pile = self.stock_pile
            
        if pile:
            card = pile[-1]
            if pile_type == 'tableau':
                x = 20 + pile_index * 100
                y = 20 + (len(pile) - 1) * 20
            elif pile_type == 'foundation':
                x = 20 + (pile_index + 2) * 100
                y = 20
            elif pile_type == 'stock':
                x = 20 + 8 * 100
                y = 20
            self.draw_card(card, x, y)
            
                
    def draw_card(self, card, x, y):
        rank = card['rank']
        suit = card['suit']
        self.canvas.create_rectangle(x, y, x + self.card_width, y + self.card_height, outline='black', fill='white')
        self.canvas.create_text(x + 10, y + 10, anchor='nw', text=rank, font=('Helvetica', '14'), fill='red')
        self.canvas.create_text(x + 10, y + 30, anchor='nw', text=suit, font=('Helvetica', '14'), fill='red')

    def handle_click(self, event):
        x, y = event.x, event.y
        for pile_index, pile in enumerate(self.tableau_piles):
            if pile:
                card_x = 20 + pile_index * 100
                card_y = 20 + (len(pile) - 1) * 20
                if card_x <= x < card_x + self.card_width and card_y <= y < card_y + self.card_height:
                    self.move_card('tableau', pile_index, None, None)
                    break
        for pile_index, pile in enumerate(self.foundation_piles):
            if pile:
                card_x = 20 + (pile_index + 2) * 100
                card_y = 20
                if card_x <= x < card_x + self.card_width and card_y <= y < card_y + self.card_height:
                    self.move_card('foundation', pile_index, None, None)
                    break
        if 20 + 8 * 100 <= x < 20 + 8 * 100 + self.card_width and 20 <= y < 20 + self.card_height:
            self.move_card('stock', None, None, None)
            
            
    def move_card(self, source_pile_type, source_pile_index, dest_pile_type, dest_pile_index):
        if source_pile_type == 'tableau':
            source_pile = self.tableau_piles[source_pile_index]
        elif source_pile_type == 'foundation':
            source_pile = self.foundation_piles[source_pile_index]
        elif source_pile_type == 'stock':
            source_pile = self.stock_pile

        if not source_pile:
            return

        card = source_pile.pop()

        if dest_pile_type is None:
            if self.can_move_to_foundation(card):
                for pile_index, pile in enumerate(self.foundation_piles):
                    if not pile or card['rank'] == 'A' or pile[-1]['rank'] == chr(ord(card['rank']) - 1):
                        self.foundation_piles[pile_index].append(card)
                        self.show_top_card('foundation', pile_index)
                        break
            elif source_pile_type == 'stock':
                self.stock_pile = []
                self.tableau_piles[0].append(card)
                self.show_top_card('tableau', 0)
        elif dest_pile_type == 'tableau':
            dest_pile = self.tableau_piles[dest_pile_index]
            if not dest_pile or (card['suit'] != dest_pile[-1]['suit'] and ord(card['rank']) == ord(dest_pile[-1]['rank']) - 1):
                dest_pile.append(card)
                self.show_top_card('tableau', dest_pile_index)

        self.show_top_card(source_pile_type, source_pile_index)
        self.check_win_condition()

    def can_move_to_foundation(self, card):
        for pile in self.foundation_piles:
            if not pile or (pile and card['rank'] == 'A') or (pile and pile[-1]['rank'] == chr(ord(card['rank']) - 1)):
                return True
        return False

    def check_win_condition(self):
        foundation_complete = all(len(pile) == 13 for pile in self.foundation_piles)
        if foundation_complete:
            print("Congratulations! You've won the game!")
    
def main():
    root = tk.Tk()
    solitaire_gui = SolitaireGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
