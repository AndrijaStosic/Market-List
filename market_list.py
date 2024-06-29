import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


items = []

def add_item():
    try:
        item_name = item_name_entry.get()
        item_price = float(price_entry.get())
        item_quantity = int(quantity_entry.get())
        total_price = item_price * item_quantity
        
        items.append((item_name, item_price, item_quantity, total_price))
        
        listbox.insert(tk.END, f"{item_name}: {item_quantity} x {item_price} = {total_price}")
        
        item_name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        
        update_total()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for price and quantity")

def update_total():
    total = sum(item[3] for item in items)
    total_label.config(text=f"Total: {total:.2f}")

def plot_totals():
    names = [item[0] for item in items]
    totals = [item[3] for item in items]
    
    plt.figure(figsize=(10, 5))
    plt.bar(names, totals, color='Red')
    plt.xlabel('Items')
    plt.ylabel('Total Price')
    plt.title('Total Price per Item')
    plt.show()

root = tk.Tk()
root.title("Market List")

tk.Label(root, text="Item Name").grid(row=0, column=0)
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1)

tk.Label(root, text="Price per Unit").grid(row=1, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.grid(row=3, column=0, columnspan=2)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2)

total_label = tk.Label(root, text="Total: 0.00")
total_label.grid(row=5, column=0, columnspan=2)

plot_button = tk.Button(root, text="See the chart", command=plot_totals)
plot_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
