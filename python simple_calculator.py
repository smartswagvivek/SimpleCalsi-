import tkinter as tk

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("400x600")
        self.master.configure(bg="#2C3E50")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry box for displaying input and results
        entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ECF0F1", fg="#2C3E50")
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

        # Button layout with colors and styling
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('←', 5, 1)  # Backspace button
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=20, bg="#3498DB", fg="white", font=('Arial', 18),
                               command=lambda t=text: self.append_to_expression(t) if t not in ('=', 'C', '←') else self.calculate() if t == '=' else self.clear() if t == 'C' else self.delete_last())
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        # Set button row and column weights to be responsive
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        new_text = current_text + str(value)
        self.result_var.set(new_text)

    def clear(self):
        self.result_var.set("")

    def delete_last(self):
        current_text = self.result_var.get()
        new_text = current_text[:-1]  # Remove the last character
        self.result_var.set(new_text)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
