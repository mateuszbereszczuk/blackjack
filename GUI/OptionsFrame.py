from GUI.DecisionTableAcesFrame import DecisionTableAcesFrame
from GUI.DecisionTableFrame import DecisionTableFrame
from Models.Game import Game
import tkinter as tk


class OptionsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.games_amount = tk.IntVar(value=100)
        self.use_decision_table_value = tk.BooleanVar()
        self.dealer_threshold = tk.IntVar(value=17)
        self.player_threshold = tk.IntVar(value=17)
        self.result_percentage = tk.StringVar()
        self.decision_table_value = tk.BooleanVar()

        self.games_amount_label = tk.Label(self, text='Number of rounds to play (max 10000):', bg='#cccccc')
        self.games_amount_entry = tk.Entry(self, width=5, textvariable=self.games_amount)
        self.use_decision_table_checkbox = tk.Checkbutton(
            self,
            text='Use decision table for player',
            command=self.use_decision_table_checkbox_clicked,
            variable=self.use_decision_table_value,
            bg='#cccccc'
        )
        self.dealer_threshold_label = tk.Label(self, text='Dealer\'s threshold for hitting:', bg='#cccccc')
        self.dealer_threshold_entry = tk.Entry(self, width=2, textvariable=self.dealer_threshold)
        self.player_threshold_label = tk.Label(self, text='Player\'s threshold for hitting:', bg='#cccccc')
        self.player_threshold_entry = tk.Entry(self, width=2, textvariable=self.player_threshold)
        self.simulation_button = tk.Button(self, text='Simulate', command=self.simulate_button_pressed, bg='#cccccc')
        self.log_text = tk.Text(self, height=10, width=32, cursor="arrow")
        self.log_scrollbar = tk.Scrollbar(self)
        self.result_percentage_label = tk.Label(self, textvariable=self.result_percentage, bg='#cccccc')
        self.decision_table_frame = DecisionTableFrame(self, bg='#cccccc')
        self.decision_table_aces_frame = DecisionTableAcesFrame(self, bg='#cccccc')

        self.games_amount_label.grid(row=0, column=0, sticky='w', padx=2, pady=(6, 0))
        self.games_amount_entry.grid(row=0, column=1, sticky='w', padx=2)
        self.use_decision_table_checkbox.grid(row=1, column=0, sticky='w', padx=2)
        self.dealer_threshold_label.grid(row=2, column=0, sticky='w', padx=2)
        self.dealer_threshold_entry.grid(row=2, column=1, sticky='w', padx=2)
        self.player_threshold_label.grid(row=3, column=0, sticky='w', padx=2)
        self.player_threshold_entry.grid(row=3, column=1, sticky='w', padx=2)
        self.simulation_button.grid(row=5, column=0, sticky='s', padx=(50, 0), pady=(12, 0))
        self.log_text.grid(row=6, columnspan=2, column=0, sticky='nsw', padx=2)
        self.log_scrollbar.grid(row=6, column=2, sticky='nsw')
        self.log_scrollbar.config(command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=self.log_scrollbar.set, state='disabled')

        self.simulation_game = Game()

    def use_decision_table_checkbox_clicked(self):
        if self.use_decision_table_value.get():
            self.player_threshold_label.configure(foreground='gray')
            self.player_threshold_entry.grid_forget()

            self.decision_table_frame.grid(row=8, column=0, columnspan=2, sticky='s')
            self.decision_table_aces_frame.grid(row=9, column=0, columnspan=2, sticky='s')

        else:
            self.player_threshold_label.configure(foreground='black')
            self.player_threshold_entry.grid(row=3, column=1, sticky='w')

            self.decision_table_frame.grid_forget()
            self.decision_table_aces_frame.grid_forget()

    def simulate_button_pressed(self):
        if self.games_amount.get() > 10_000:
            self.games_amount.set(10_000)
        self.log_text.configure(state='normal')
        self.log_text.delete('1.0', tk.END)
        self.log_text.configure(state='disabled')
        win_counter = 0
        tie_counter = 0
        loss_counter = 0

        for i in range(self.games_amount.get()):
            self.simulation_game.start()

            result = self.play_simulation(
                self.dealer_threshold.get(),
                self.player_threshold.get(),
                self.use_decision_table_value.get()
            )
            if result == 'WIN':
                win_counter += 1
            if result == 'TIE':
                tie_counter += 1
            if result == 'LOSS':
                loss_counter += 1
            round_summary = 'Dealer: {'
            cards_code = []

            for card in self.simulation_game.dealer_hand.cards:
                cards_code.append(str(card.code + card.suit[0]))
            round_summary += ' '.join(cards_code) + '} (' + str(self.simulation_game.dealer_hand.value) + ')\nPlayer: {'
            cards_code = []
            for card in self.simulation_game.player_hand.cards:
                cards_code.append(str(card.code + card.suit[0]))
            round_summary += ' '.join(cards_code) + '} (' + str(self.simulation_game.player_hand.value) + ')\n'
            round_summary += result + '\n***\n'
            self.simulation_game.put_cards_back()
            self.log_text.configure(state='normal')
            self.log_text.insert(tk.END, round_summary + '\n')
            self.log_text.configure(state='disabled')

        win_percentage = round(win_counter / self.games_amount.get() * 100, 3)
        tie_percentage = round(tie_counter / self.games_amount.get() * 100, 3)
        loss_percentage = round(loss_counter / self.games_amount.get() * 100, 3)
        self.result_percentage.set(
            'Win percentage: ' + str(win_percentage) + '%' +
            '| Tie: ' + str(tie_percentage) + '%' +
            '| Lose: ' + str(loss_percentage) + '%'
        )
        self.result_percentage_label.grid(row=7, column=0, columnspan=2, sticky='w')

    def play_simulation(self, dealer_threshold=17, player_threshold=17, use_decision_table=False):

        player_hand_value = self.simulation_game.player_hand.value
        dealer_hand_value = self.simulation_game.dealer_hand.value
        dealer_visible_card_value = self.simulation_game.dealer_hand.cards[1].value
        
        if player_hand_value != 21:
            if use_decision_table:
                if self.simulation_game.player_hand.aces > 0:
                    decision_table = self.decision_table_aces_frame.decision_table_aces_value_list
                else:
                    decision_table = self.decision_table_frame.decision_table_value_list
                decision = decision_table[20 - player_hand_value][dealer_visible_card_value - 2]
                while decision != 'S':
                    self.simulation_game.player_hand.add_card(self.simulation_game.deck.deal())
                    player_hand_value = self.simulation_game.player_hand.value
                    if player_hand_value > 20:
                        decision = 'S'
                    else:
                        decision = decision_table[20 - player_hand_value][dealer_visible_card_value - 2]

            else:
                while player_hand_value < player_threshold:
                    self.simulation_game.player_hand.add_card(self.simulation_game.deck.deal())
                    player_hand_value = self.simulation_game.player_hand.value

        if player_hand_value > 21:
            return 'LOSS'

        while (dealer_hand_value < player_hand_value) and dealer_hand_value < dealer_threshold:
            self.simulation_game.dealer_hand.add_card(self.simulation_game.deck.deal())
            dealer_hand_value = self.simulation_game.dealer_hand.value

        if dealer_hand_value > 21:
            return 'WIN'
        if dealer_hand_value == player_hand_value:
            return 'TIE'
        if dealer_hand_value > player_hand_value:
            return 'LOSS'
        else:
            return 'WIN'
