import tkinter as tk
import math

class ScientificCalculator:
    """A scientific calculator application with a comprehensive set of functions."""

    def __init__(self, master):
        """Initializes the calculator window and its components.

        Args:
            master (tk.Tk): The main Tkinter window.
        """

        self.master = master
        self.master.title("Scientific Calculator")
        self.master.geometry("600x400")

        self.theme = "dark"  # Default theme
        self.configure_theme()

        # Create the display widget
        self.display = tk.Entry(
            master, font=("Arial", 18), borderwidth=2, relief=tk.SUNKEN, width=30, justify=tk.RIGHT
        )
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Create the buttons using a separate method for better organization
        self.create_buttons()

        # Create the theme toggle button
        self.theme_button = tk.Button(
            master,
            text="Dark Mode",
            width=10,
            height=2,
            command=self.toggle_theme
        )
        self.theme_button.grid(row=7, column=0, columnspan=2)

    def create_buttons(self):
        """Creates the calculator buttons and binds them to corresponding functions."""

        button_data = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sqrt", 1, 4), ("pow", 1, 5),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("sin", 2, 4), ("cos", 2, 5),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("tan", 3, 4), ("log", 3, 5),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3, 2), ("C", 4, 5),
            ("e", 5, 0), ("pi", 5, 1), ("factorial", 5, 2), ("ln", 5, 3), ("arcsin", 5, 4), ("arccos", 5, 5),
            ("arcsin", 6, 0), ("arccos", 6, 1), ("arctan", 6, 2), ("sinh", 6, 3), ("cosh", 6, 4), ("tanh", 6, 5),
            ("AND", 7, 0), ("OR", 7, 1), ("XOR", 7, 2), ("NOT", 7, 3), ("<<", 7, 4), (">>", 7, 5),
            ("abs", 8, 0), ("ceil", 8, 1), ("floor", 8, 2), ("round", 8, 3), ("exp", 8, 4), ("log10", 8, 5),
        ]

        for text, row, col, *args in button_data:
            button = tk.Button(
                self.master,
                text=text,
                width=6,
                height=2,
                font=("Arial", 14),
                command=lambda t=text: self.handle_button_click(t),
            )
            button.grid(row=row, column=col, columnspan=args[0] if args else 1)

    def handle_button_click(self, button_text):
        """Handles clicks on the calculator buttons and updates the display.

        Args:
            button_text (str): The text of the clicked button.
        """

        current_value = self.display.get()

        if button_text == "C":
            self.display.delete(0, tk.END)
        elif button_text == "=":
            try:
                expression = current_value.replace("sqrt", "math.sqrt").replace("pow", "**").replace("log", "math.log10")
                expression = expression.replace("AND", "&").replace("OR", "|").replace("XOR", "^").replace("NOT", "~")
                result = eval(expression, {"math": math})
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, f"Error: {e}")
        else:
            self.display.insert(tk.END, button_text)

    def toggle_theme(self):
        """Toggles between dark and light themes."""

        if self.theme == "dark":
            self.theme = "light"
            self.master.configure(bg="#f0f0f0")  # Light background
            self.display.configure(bg="#f0f0f0", fg="black")
            for widget in self.master.winfo_children():
                widget.configure(bg="#f0f0f0", fg="black")
            self.theme_button.config(text="Dark Mode")
        else:
            self.theme = "dark"
            self.master.configure(bg="#121212")  # Dark background
            self.display.configure(bg="#121212", fg="white")
            for widget in self.master.winfo_children():
                widget.configure(bg="#121212", fg="white")
            self.theme_button.config(text="Light Mode")


# Create the main window and start the application
root = tk.Tk()
app = ScientificCalculator(root)
root.mainloop()
