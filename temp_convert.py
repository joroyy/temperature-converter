import tkinter as tk
from tkinter import messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        self.setup_ui()

    def setup_ui(self):
        self.label_celsius = tk.Label(self.root, text="Enter Celsius:")
        self.label_celsius.pack(pady=5)

        self.entry_celsius = tk.Entry(self.root)
        self.entry_celsius.pack(pady=5)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

        self.unit_var = tk.StringVar()
        self.unit_var.set("Fahrenheit")
        
        self.unit_frame = tk.Frame(self.root)
        self.unit_frame.pack(pady=5)

        self.label_unit = tk.Label(self.unit_frame, text="Convert to:")
        self.label_unit.pack(side=tk.LEFT)

        self.radio_fahrenheit = tk.Radiobutton(self.unit_frame, text="Fahrenheit", variable=self.unit_var, value="Fahrenheit")
        self.radio_fahrenheit.pack(side=tk.LEFT)

        self.radio_celsius = tk.Radiobutton(self.unit_frame, text="Celsius", variable=self.unit_var, value="Celsius")
        self.radio_celsius.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear)
        self.clear_button.pack(pady=5)

    def convert(self):
        try:
            celsius = float(self.entry_celsius.get())

            if self.unit_var.get() == "Fahrenheit":
                result = celsius * 9/5 + 32
                converted_unit = "°F"
            else:
                result = (celsius - 32) * 5/9
                converted_unit = "°C"

            self.result_label.config(text=f"Converted: {result:.2f}{converted_unit}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for Celsius.")

    def clear(self):
        self.entry_celsius.delete(0, tk.END)
        self.result_label.config(text="")
        self.unit_var.set("Fahrenheit")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
