import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("370x500")
        self.root.resizable(0, 0)
        self.root.title("calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.total_label, self.label = self.create_display_label()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.button_frame = self.create_buttons_frame()

        self.button_frame.rowconfigure(0, weight=1)
        for i in range(1,5):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

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
    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()
    def create_digit_buttons(self):
        for digit ,grid_value in self.digits.items():
            buttons = tk.Button(self.button_frame, text=str(digit), bg="#FFFFFF",fg="#25265E",
                               font=("Arial", 24, "bold"), borderwidth=0 , command=lambda x=digit: self.add_to_expression(x))
            buttons.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self,operator):
        self.current_expression+= operator
        self.total_expression+= self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            buttons=tk.Button(self.button_frame, text=symbol,bg="#F8FAFF" ,fg="#25265E",font=("Arial", 20),borderwidth=0,command=lambda x=operator: self.append_operator(x))
            buttons.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg="#F8FAFF" ,fg="#25265E",font=("Arial", 20),
                           borderwidth=0, command = self.clear() )
        button.grid(row=0, column=1,columnspan=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()

        self.current_expression = str(eval(self.total_expression))
        self.total_expression=""
        self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg="#CCEDFF" ,fg="#25265E",font=("Arial", 20),
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text= self.current_expression)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
