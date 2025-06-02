import tkinter as tk

count = 0

def increment():
    global count
    count += 1
    label.config(text=f"Count: {count}")

root = tk.Tk()
root.title("Counter App")
root.geometry("200x100")

label = tk.Label(root, text="Count: 0", font=("Arial", 16))
label.pack(pady=10)

button = tk.Button(root, text="カウント", command=increment)
button.pack()

root.mainloop()
