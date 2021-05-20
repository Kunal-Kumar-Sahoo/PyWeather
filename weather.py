import tkinter as tk
import requests
import time


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x500")
    window.title("PyWeather")

    f = ("ubuntu", 15, "bold")
    t = ("ubuntu", 35, "bold")

    textField = tk.Entry(window, font=t)
    textField.pack(pady=20)
    textField.focus()

    label1 = tk.Label(window, font=t)
    label1.pack()
    label2 = tk.Label(window, font=f)
    label2.pack()

    window.mainloop()
