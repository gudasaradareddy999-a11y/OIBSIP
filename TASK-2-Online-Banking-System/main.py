import tkinter as tk
from tkinter import messagebox
import datetime

# ------------------------------
# Simple in-memory database
# ------------------------------
users = {
    "admin": {"password": "1234", "balance": 1000.0, "history": []}
}

current_user = None

# ------------------------------
# Helper Functions
# ------------------------------
def login():
    global current_user
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username]["password"] == password:
        current_user = username
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        login_frame.pack_forget()
        banking_frame.pack()
        update_balance()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()

    if username in users:
        messagebox.showerror("Error", "User already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "Username/Password cannot be empty")
    else:
        users[username] = {"password": password, "balance": 0.0, "history": []}
        messagebox.showinfo("Success", "Account created successfully!")

def update_balance():
    lbl_balance.config(text=f"Balance: ₹{users[current_user]['balance']:.2f}")

def deposit():
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            raise ValueError
        users[current_user]["balance"] += amount
        record_transaction("Deposit", amount)
        update_balance()
        messagebox.showinfo("Success", f"Deposited ₹{amount:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def withdraw():
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            raise ValueError
        if users[current_user]["balance"] >= amount:
            users[current_user]["balance"] -= amount
            record_transaction("Withdraw", amount)
            update_balance()
            messagebox.showinfo("Success", f"Withdrew ₹{amount:.2f}")
        else:
            messagebox.showerror("Error", "Insufficient funds")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def record_transaction(action, amount):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    users[current_user]["history"].append(f"{timestamp} - {action}: ₹{amount:.2f}")

def show_history():
    history = users[current_user]["history"]
    if history:
        messagebox.showinfo("Transaction History", "\n".join(history))
    else:
        messagebox.showinfo("Transaction History", "No transactions yet.")

# ------------------------------
# GUI Setup
# ------------------------------
root = tk.Tk()
root.title("Online Banking System")
root.geometry("400x300")

# Login Frame
login_frame = tk.Frame(root)
tk.Label(login_frame, text="Username").pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()

tk.Label(login_frame, text="Password").pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=5)
tk.Button(login_frame, text="Register", command=register).pack(pady=5)
login_frame.pack()

# Banking Frame
banking_frame = tk.Frame(root)

lbl_balance = tk.Label(banking_frame, text="Balance: ₹0.00", font=("Arial", 14))
lbl_balance.pack(pady=10)

entry_amount = tk.Entry(banking_frame)
entry_amount.pack()

tk.Button(banking_frame, text="Deposit", command=deposit).pack(pady=5)
tk.Button(banking_frame, text
