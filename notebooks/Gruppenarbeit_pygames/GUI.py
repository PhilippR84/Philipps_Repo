import tkinter as tk

def button1_clicked():
    print("Button 1 was clicked!")

def button2_clicked():
    print("Button 2 was clicked!")

def button3_clicked():
    print("Button 3 was clicked!")

root = tk.Tk()
root.title("My GUI with Three Buttons")

button1 = tk.Button(root, text="Button 1", command=button1_clicked)
button1.pack()

button2 = tk.Button(root, text="Button 2", command=button2_clicked)
button2.pack()

button3 = tk.Button(root, text="Button 3", command=button3_clicked)
button3.pack()
root.mainloop()