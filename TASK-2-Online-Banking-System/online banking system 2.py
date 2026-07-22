import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Database (In-Memory)
# -----------------------------
users = {}
current_user = None

# -----------------------------
# Functions
# -----------------------------
def register():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter Username and Password")
        return

    if username in users:
        messagebox.showerror("Error", "User already exists")
        return

    users[username] = {
        "password": password,
        "balance": 0,
        "history": ["Account Created"]
    }

    messagebox.showinfo("Success", "Account Created Successfully")


def login():
    global current_user

    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if username not in users:
        messagebox.showerror("Error", "User does not exist")
        return

    if users[username]["password"] != password:
        messagebox.showerror("Error", "Incorrect Password")
        return

    current_user = username
    messagebox.showinfo("Success", f"Welcome {username}")

    login_frame.pack_forget()
    banking_frame.pack()


def deposit():
    if entry_amount.get().strip() == "":
        messagebox.showerror("Error", "Please enter an amount")
        return

    try:
        amt = int(entry_amount.get())

        if amt <= 0:
            messagebox.showerror("Error", "Enter a valid amount")
            return

        users[current_user]["balance"] += amt
        users[current_user]["history"].append(f"Deposited ₹{amt}")

        messagebox.showinfo("Success", "Amount Deposited")
        entry_amount.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only")


def withdraw():
    if entry_amount.get().strip() == "":
        messagebox.showerror("Error", "Please enter an amount")
        return

    try:
        amt = int(entry_amount.get())

        if amt <= 0:
            messagebox.showerror("Error", "Enter a valid amount")
            return

        if amt > users[current_user]["balance"]:
            messagebox.showerror("Error", "Insufficient Balance")
            return

        users[current_user]["balance"] -= amt
        users[current_user]["history"].append(f"Withdrawn ₹{amt}")

        messagebox.showinfo("Success", "Amount Withdrawn")
        entry_amount.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only")


def check_balance():
    bal = users[current_user]["balance"]
    messagebox.showinfo("Balance", f"Current Balance = ₹{bal}")


def transaction_history():
    history = "\n".join(users[current_user]["history"])
    messagebox.showinfo("Transaction History", history)


def logout():
    global current_user
    current_user = None

    banking_frame.pack_forget()

    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    login_frame.pack()


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Online Banking System")
root.geometry("400x450")
root.config(bg="lightblue")

# -----------------------------
# Login Frame
# -----------------------------
login_frame = tk.Frame(root, bg="lightblue")

title = tk.Label(
    login_frame,
    text="ONLINE BANKING SYSTEM",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=15)

tk.Label(
    login_frame,
    text="Username",
    bg="lightblue",
    font=("Arial", 12)
).pack()

entry_username = tk.Entry(login_frame, width=30)
entry_username.pack(pady=5)

tk.Label(
    login_frame,
    text="Password",
    bg="lightblue",
    font=("Arial", 12)
).pack()

entry_password = tk.Entry(login_frame, show="*", width=30)
entry_password.pack(pady=5)

tk.Button(
    login_frame,
    text="Create Account",
    width=20,
    command=register,
    bg="green",
    fg="white"
).pack(pady=10)

tk.Button(
    login_frame,
    text="Login",
    width=20,
    command=login,
    bg="blue",
    fg="white"
).pack()

login_frame.pack()

# -----------------------------
# Banking Frame
# -----------------------------
banking_frame = tk.Frame(root, bg="lightyellow")

tk.Label(
    banking_frame,
    text="Bank Dashboard",
    font=("Arial", 16, "bold"),
    bg="lightyellow"
).pack(pady=10)

entry_amount = tk.Entry(banking_frame, width=25)
entry_amount.pack(pady=10)

tk.Button(
    banking_frame,
    text="Deposit",
    width=20,
    command=deposit,
    bg="green",
    fg="white"
).pack(pady=5)

tk.Button(
    banking_frame,
    text="Withdraw",
    width=20,
    command=withdraw,
    bg="red",
    fg="white"
).pack(pady=5)

tk.Button(
    banking_frame,
    text="Check Balance",
    width=20,
    command=check_balance,
    bg="orange"
).pack(pady=5)

tk.Button(
    banking_frame,
    text="Transaction History",
    width=20,
    command=transaction_history,
    bg="purple",
    fg="white"
).pack(pady=5)

tk.Button(
    banking_frame,
    text="Logout",
    width=20,
    command=logout,
    bg="black",
    fg="white"
).pack(pady=10)

root.mainloop()