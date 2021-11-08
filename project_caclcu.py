import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("370x500")
        self.root.resizable(0, 0)
        self.root.title("calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.total_label, self.label = self.create_display_label()
        self.button_frame = self.create_buttons_frame()
        self.create_digit_buttons()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5",
                               fg="#25265E", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5", fg="#25265E",
                         padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit ,grid_value in self.digits.items():
            buttons = tk.Button(self.button_frame, text=str(digit), bg="#FFFFFF",fg="#25265E",
                               font=("Arial", 24, "bold"), borderwidth=0)
            buttons.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
