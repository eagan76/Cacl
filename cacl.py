import tkinter as tk
from math import sin, cos, tan, sqrt, log, log10, exp, pi, e

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ezcalc")
        self.root.geometry("400x600")
        self.root.configure(bg="#3d3d3d")

        self.scientific_mode = False
        self.expression = ""

        # Display
        self.display = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14,
                                borderwidth=4, justify="right", bg="#4d4d4d", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Label and Scientific Mode Toggle Button
        tk.Label(root, text="Ezcalc", font=("Arial", 18), bg="#3d3d3d", fg="white").grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        self.sci_button = tk.Button(root, text="Sci", command=self.toggle_scientific_mode, bg="#555555", fg="white", width=5)
        self.sci_button.grid(row=1, column=2, columnspan=2, sticky="e", padx=10)

        # Standard buttons
        buttons = [
            ('C', 2, 0), ('←', 2, 1), ('±', 2, 2), ('÷', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('×', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('−', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2, 2)
        ]

        for (text, row, col, *args) in buttons:
            colspan = args[0] if args else 1
            tk.Button(root, text=text, width=5 * colspan, height=2, bg="#666666", fg="white",
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, columnspan=colspan)

        # Scientific buttons, initially hidden
        self.sci_buttons = [
            ('(', 7, 0), (')', 7, 1), ('^', 7, 2), ('√', 7, 3),
            ('sin', 8, 0), ('cos', 8, 1), ('tan', 8, 2), ('ln', 8, 3),
            ('log', 9, 0), ('exp', 9, 1), ('π', 9, 2), ('e', 9, 3),
        ]
        self.sci_button_widgets = []

        for (text, row, col) in self.sci_buttons:
            btn = tk.Button(root, text=text, width=5, height=2, bg="#666666", fg="white",
                            command=lambda t=text: self.on_button_click(t))
            self.sci_button_widgets.append(btn)
            btn.grid(row=row, column=col, sticky="nsew")
            btn.grid_remove()  # Hide initially

    def toggle_scientific_mode(self):
        self.scientific_mode = not self.scientific_mode
        for btn in self.sci_button_widgets:
            if self.scientific_mode:
                btn.grid()
            else:
                btn.grid_remove()
        self.sci_button.config(text="Basic" if self.scientific_mode else "Sci")

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display()
        elif char == '←':
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.update_display()
        elif char == '=':
            self.calculate_result()
        else:
            self.expression += char
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        try:
            # Replace symbols with math functions and constants
            expression = self.expression.replace('÷', '/').replace('×', '*').replace('−', '-')
            expression = expression.replace('√', 'sqrt').replace('π', str(pi)).replace('e', str(e))
            expression = expression.replace('sin', 'sin').replace('cos', 'cos').replace('tan', 'tan')
            expression = expression.replace('ln', 'log').replace('log', 'log10').replace('^', '**')
            result = eval(expression, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan,
                                                               "sqrt": sqrt, "log": log, "log10": log10,
                                                               "exp": exp, "pi": pi, "e": e})
            self.expression = str(round(result, 10))
            self.update_display()
        except Exception:
            self.expression = "Error"
            self.update_display()

# Initialize Tkinter window
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
