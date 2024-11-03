import tkinter as tk

def calculate_product():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        product = num1 * num2
        result_label.config(text=f"Result: {product}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Product Calculator")

# Number 1 Label and Entry
tk.Label(window, text="Number 1:").grid(row=0, column=0)
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1)

# Number 2 Label and Entry
tk.Label(window, text="Number 2:").grid(row=1, column=0)
num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1)

# Calculate Button
calculate_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calculate_button.grid(row=2, column=0, columnspan=2)

# Result Label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2)

# Run the main loop
window.mainloop()
