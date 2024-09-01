import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create input field
        self.entry = tk.Entry(self.root, width=30, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.buttons = {
            "7": (1, 0), "8": (1, 1), "9": (1, 2), "/": (1, 3),
            "4": (2, 0), "5": (2, 1), "6": (2, 2), "*": (2, 3),
            "1": (3, 0), "2": (3, 1), "3": (3, 2), "-": (3, 3),
            "0": (4, 0), ".": (4, 1), "=": (4, 2), "+": (4, 3),
            "AC": (5, 0), "C": (5, 1), "M+": (5, 2), "M-": (5, 3),
            "MR": (6, 0), "MC": (6, 1), "MS": (6, 2), "%": (6, 3),
            "sin": (7, 0), "cos": (7, 1), "tan": (7, 2), "log": (7, 3),
            "ln": (8, 0), "sqrt": (8, 1), "x^2": (8, 2), "x^y": (8, 3),
        }

        for key, (row, col) in self.buttons.items():
            button = tk.Button(self.root, text=key, font=("Arial", 14), command=lambda key=key: self.handle_button(key))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Bind keyboard events
        self.root.bind("<Key>", self.handle_key)

        # Initialize memory
        self.memory = 0

    def handle_button(self, key):
        if key in self.buttons:
            if key == "=":
                try:
                    result = eval(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(result))
                except Exception as e:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
            elif key in ["AC", "C"]:
                self.entry.delete(0, tk.END)
            elif key == "M+":
                try:
                    self.memory += float(self.entry.get())
                except ValueError:
                    pass
            elif key == "M-":
                try:
                    self.memory -= float(self.entry.get())
                except ValueError:
                    pass
            elif key == "MR":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(self.memory))
            elif key == "MC":
                self.memory = 0
            elif key == "%":
                try:
                    value = float(self.entry.get())
                    result = value / 100
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(result))
                except ValueError:
                    pass
            elif key in ["sin", "cos", "tan"]:
                try:
                    value = float(self.entry.get())
                    value_radians = math.radians(value)  # Convert to radians
                    if key == "sin":
                        result = math.sin(value_radians)
                    elif key == "cos":
                        result = math.cos(value_radians)
                    elif key == "tan":
                        result = math.tan(value_radians)
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(result))
                except ValueError:
                    pass
            elif key in ["log", "ln", "sqrt", "x^2", "x^y"]:
                try:
                    value = float(self.entry.get())
                    if key == "log":
                        result = math.log10(value)
                    elif key == "ln":
                        result = math.log(value)
                    elif key == "sqrt":
                        result = math.sqrt(value)
                    elif key == "x^2":
                        result = value ** 2
                    elif key == "x^y":
                        exponent = float(self.entry.get())
                        result = value ** exponent
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(result))
                except ValueError:
                    pass
            else:
                self.entry.insert(tk.END, key)

    def handle_key(self, event):
        key = event.char
        if key in self.buttons:
            self.handle_button(key)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
