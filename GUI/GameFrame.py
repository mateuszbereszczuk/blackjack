import tkinter as tk
from GUI.HandFrame import HandFrame
from GUI.ImageManager import ImageManager
from Models.Card import Card
from Models.Game import Game


class GameFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.hand_frame_height = 315
        self.result_text = tk.StringVar()
        self.image_manager = ImageManager()
        self.result_label = tk.Label(self, font=('', 24), textvariable=self.result_text)
        self.dealer_hand_frame = HandFrame(self, bg='#f0f0f0', bd=10)
        self.player_hand_frame = HandFrame(self, bg='#f0f0f0', bd=10)
        self.hit_button = tk.Button(self, text='Hit', font=('', 16), command=self.hit_button_pressed)
        self.pass_button = tk.Button(self, text='Pass', font=('', 16), command=self.pass_button_pressed)
        self.play_button = tk.Button(self, text='Play', font=('', 20), command=self.play_button_pressed)
        self.parent = parent
        self.game = Game()
        self.resized_card_images = {}

        self.hidden_card = Card('', '', 'red_back', 0)
        self.add_card_image(self.hidden_card)

        self.play_button.place(rely=0.47, relx=0.46)

    def update_hands(self, dealer_hand, player_hand, hidden_card=True):
        self.dealer_hand_frame.place(rely=0.10, relheight=0.35, relwidth=1)
        self.dealer_hand_frame.show_cards(dealer_hand, hidden_card)
        self.player_hand_frame.place(rely=0.55, relheight=0.35, relwidth=1)
        self.player_hand_frame.show_cards(player_hand, False)

    def end_game(self, result):
        if result == 'win':
            self.result_text.set('You won')
        elif result == 'tie':
            self.result_text.set("It's a tie")
        elif result == 'lose':
            self.result_text.set('You lost')
        self.result_label.pack(side='top', pady=(10, 0))
        self.hit_button.place_forget()
        self.pass_button.place_forget()
        self.update_hands(self.game.dealer_hand, self.game.player_hand, False)
        self.game.put_cards_back()

        self.play_button.place(rely=0.47, relx=0.46)

    def hit_button_pressed(self):
        self.game.player_hand.add_card(self.game.deck.deal())
        self.add_card_image(self.game.player_hand.cards[-1])
        self.update_hands(self.game.dealer_hand, self.game.player_hand, True)
        if self.game.player_hand.is_hand_over():
            self.end_game('lose')

    def pass_button_pressed(self):
        while (self.game.dealer_hand.value < self.game.player_hand.value) and \
                self.game.dealer_hand.value < 17:
            self.game.dealer_hand.add_card(self.game.deck.deal())
            self.add_card_image(self.game.dealer_hand.cards[-1])

        if self.game.dealer_hand.is_hand_over():
            self.end_game('win')
        elif self.game.player_hand.value > self.game.dealer_hand.value:
            self.end_game('win')
        elif self.game.player_hand.value == self.game.dealer_hand.value:
            self.end_game('tie')
        else:
            self.end_game('lose')

    def play_button_pressed(self):
        self.result_label.pack_forget()
        self.hit_button.place(rely=0.48, relx=0.32)
        self.pass_button.place(rely=0.48, relx=0.65)
        self.play_button.place_forget()

        self.game.start()

        for card in self.game.dealer_hand.cards:
            self.add_card_image(card)
        for card in self.game.player_hand.cards:
            self.add_card_image(card)

        self.update_hands(self.game.dealer_hand, self.game.player_hand, True)

    def add_card_image(self, card):
        card_code_suit = card.code + card.suit[0] if card.code != 'red_back' else card.code
        if card_code_suit not in self.resized_card_images:
            card_name = card_code_suit + '.png'
            self.resized_card_images[card_code_suit] = self.image_manager.add_image(card_name, self.hand_frame_height * 0.8)
