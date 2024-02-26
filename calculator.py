import tkinter as tk

def button_click(symbol):
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
        current = ""
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Casio Calculator")

entry = tk.Entry(root, width=30, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
