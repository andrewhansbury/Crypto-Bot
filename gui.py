import tkinter as tk
from tkinter import Frame, Label, ttk
from typing_extensions import IntVar


root = tk.Tk()


root.geometry("300x100")

root.title("Obama BOT [KJ]")
root.resizable(0, 0)
login_frame = Frame(root)
setup_screen = Frame(root)
login_frame.pack()


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


def display_login():

    # login_frame window
    login_frame.focus_set()

    # api key
    api_key_label = ttk.Label(login_frame, text="API Key:")
    api_key_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    api_key_entry = ttk.Entry(login_frame)
    api_key_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    # api secret
    api_secret_label = ttk.Label(login_frame, text="API Secret:")
    api_secret_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    api_secret_entry = ttk.Entry(login_frame,  show="*")
    api_secret_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    # login button
    login_button = ttk.Button(login_frame, text="Login", command=enter)
    login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    api_secret_entry.bind('<Return>', enter)


def display_setup():
    setup_screen.focus_set()

    account_balance = ttk.Label(setup_screen, text="Account Balance:")
    account_balance.pack()

    risk_label = ttk.Label(setup_screen, text="% Risk (Of Account):")
    risk_label.pack()

  # Amount Slider
    global risk_entry
    risk_entry = ttk.Entry(setup_screen)
    risk_entry.pack()

    risk_button = ttk.Button(
        setup_screen, text="Set Risk", command=set_risk_button)
    risk_button.pack()

    risk_entry.bind('<Return>', set_risk_button)


def set_risk_button(event=None):
    print(risk_entry.get())


def enter(event=None):
    login_frame.destroy()
    setup_screen.pack()
    display_setup()


def main():

    while True:
        display_login()
        root.mainloop()


if __name__ == "__main__":
    main()
