import tkinter as tk
from tkinter import messagebox

from main import login, bank_manager


def main_window(username):
    def handle_deposit():
        amount = amount_entry.get()
        bank_manager(int(amount), 1, username)
        messagebox.showinfo("Deposit success", "You deposited " + amount + " money to your account")

    def handle_withdraw():
        amount = amount_entry.get()
        bank_manager(int(amount), 2, username)
        messagebox.showinfo("Deposit success", "You deposited " + amount + " money from your account")

    def handle_show_balance():
        balance = bank_manager(0, 3, username)
        messagebox.showinfo(username + "balance", "Your balance is: " + str(balance))

    main = tk.Toplevel() # חלון ראשי
    main.title("Main Window") # כותרת
    main.geometry("300x150") # מימדים

    username_greet_label = tk.Label(main, text="Hello " + username)
    username_greet_label.pack()

    amount_label = tk.Label(main, text="Amount:")
    amount_label.pack()

    amount_entry = tk.Entry(main)
    amount_entry.pack()

    deposit_button = tk.Button(main, text="Deposit", command=handle_deposit)
    deposit_button.pack()

    withdraw_button = tk.Button(main, text="Withdraw", command=handle_withdraw)
    withdraw_button.pack()

    get_balance_button = tk.Button(main, text="Show balance", command=handle_show_balance)
    get_balance_button.pack()


def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password) is not None:
        main_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


root = tk.Tk()
root.title("Login Page")
root.geometry("300x150")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

root.mainloop()
