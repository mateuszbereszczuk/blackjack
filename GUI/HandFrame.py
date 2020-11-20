import tkinter as tk


class HandFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.value_text = tk.StringVar()
        self.cards_value_label = tk.Label(self, textvariable=self.value_text, font=('', 16), anchor="center", width=2)

        self.card_labels = []

    def show_cards(self, hand, hidden_card):
        for card_label in self.card_labels:
            card_label.place_forget()

        self.parent.parent.parent.update()
        hand_frame_width = self.winfo_width()

        for i, card in enumerate(hand.cards):
            if hidden_card and i == 0:
                card_image = self.parent.resized_card_images['red_back']
            else:
                card_image = self.parent.resized_card_images[card.code + card.suit[0]]

            image_label = tk.Label(self, image=card_image)
            image_label.image = card_image
            self.card_labels.append(image_label)
            middle = (hand_frame_width / 2) - (card_image.width() / 2)
            space_between_cards_center = card_image.width() + 20
            first_card_place = (space_between_cards_center / 2) * (len(hand.cards) - 1)

            image_label.place(
                relx=(middle - (first_card_place - (space_between_cards_center * i))) / hand_frame_width,
                rely=0.06
            )

        if hidden_card:
            self.value_text.set(hand.cards[1].value)
        else:
            self.value_text.set(hand.value)
        self.cards_value_label.place(relx=0.489, rely=0.90)
