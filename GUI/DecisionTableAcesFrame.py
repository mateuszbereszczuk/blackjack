import tkinter as tk


class DecisionTableAcesFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.decision_table_aces_label = tk.Label(self, text='Decision table with aces', bg='#cccccc')
        self.decision_table_aces_label.grid(row=0, columnspan=11, column=1)

        self.dealer_label = tk.Label(self, text='Dealer\'s face-up card', bg='#cccccc')
        self.player_label = tk.Label(self, text='Player', bg='#cccccc')

        self.dealer_label.grid(row=1, columnspan=10, column=1, pady=(10, 0))
        self.player_label.grid(row=2, column=0)

        self.decision_table_aces_value_list = {}

        for i in range(10):
            possible_card_values_label = tk.Label(
                self,
                text=str('A' if i == 9 else i + 2),
                relief=tk.RIDGE,
                borderwidth=1,
                width=2,
                bg='#cccccc'
            )
            possible_card_values_label.grid(row=2, column=i + 1)

        for i in range(9):
            possible_card_values_label = tk.Label(
                self,
                text='A, ' + str(9 - i),
                relief=tk.RIDGE,
                borderwidth=1,
                width=4,
                bg='#cccccc'
            )
            possible_card_values_label.grid(row=i + 3, column=0, sticky='e')
            row_values_dictionary = {}
            for j in range(10):
                if i < 4:
                    decision_label = tk.Label(self, text='S', bg='red', cursor='hand2')
                    row_values_dictionary[j] = 'S'
                else:
                    decision_label = tk.Label(self, text='H', bg='greenyellow', cursor='hand2')
                    row_values_dictionary[j] = 'H'
                self.decision_table_aces_value_list[i] = row_values_dictionary
                decision_label.bind("<Button-1>", self.change_decision)
                decision_label.grid(row=i + 3, column=j + 1, sticky='nsew')

    def change_decision(self, event):
        position = event.widget.grid_info()
        if event.widget.cget('text') == 'S':
            event.widget.config(bg='greenyellow', text='H')
            self.decision_table_aces_value_list[position['row'] - 3][position['column'] - 1] = 'H'
        else:
            event.widget.config(bg='red', text='S')
            self.decision_table_aces_value_list[position['row'] - 3][position['column'] - 1] = 'S'
