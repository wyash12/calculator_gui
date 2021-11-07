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
        self.button_frame = self.create_buttons_frame()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5",
                               fg="#2526SE", padx=24, font=("Arial", 16))
        total_label.pack(Expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F5F5F5", fg="#2526SE",
                         padx=24, font=("Arial", 40, "bold"))
        label.pack(Expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
