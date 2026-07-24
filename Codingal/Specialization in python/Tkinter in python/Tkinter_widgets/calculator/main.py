from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("Denomination Counter")
root.geometry("700x550")
root.configure(bg="#6C63FF")
root.resizable(False, False)

def topwin():

    top = Toplevel(root)
    top.title("Currency Note Calculator")
    top.geometry("650x600")
    top.configure(bg="#EAF6FF")
    top.resizable(False, False)

    Label(
        top,
        text="Currency Note Calculator",
        font=("Segoe UI", 22, "bold"),
        bg="#3498DB",
        fg="white",
        pady=10
    ).pack(fill=X)

    frame = Frame(top, bg="white", bd=3, relief=RIDGE)
    frame.place(relx=0.5, rely=0.53, anchor=CENTER,
                width=500, height=430)

    Label(
        frame,
        text="Enter Total Amount (₹)",
        font=("Segoe UI", 13, "bold"),
        bg="white"
    ).pack(pady=15)

    amount_entry = Entry(
        frame,
        font=("Segoe UI", 15),
        justify="center",
        width=20
    )
    amount_entry.pack()

    result = Frame(frame, bg="#F4F6F7")
    result.pack(pady=20)

    Label(
        result,
        text="Denomination",
        font=("Segoe UI", 13, "bold"),
        bg="#F4F6F7"
    ).grid(row=0, column=0, padx=20)

    Label(
        result,
        text="Count",
        font=("Segoe UI", 13, "bold"),
        bg="#F4F6F7"
    ).grid(row=0, column=1)

    notes = [2000, 500, 200, 100, 50, 20, 10]
    entries = {}

    for i, note in enumerate(notes, start=1):

        Label(
            result,
            text=f"₹{note}",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            width=10
        ).grid(row=i, column=0, pady=5)

        e = Entry(
            result,
            width=10,
            justify="center",
            font=("Segoe UI", 12),
            state="readonly"
        )

        e.grid(row=i, column=1, padx=10)

        entries[note] = e

    remaining_label = Label(
        frame,
        text="Remaining: ₹0",
        font=("Segoe UI", 12, "bold"),
        fg="red",
        bg="white"
    )

    remaining_label.pack(pady=10)


    def calculator(event=None):

        value = amount_entry.get()

        if value == "":
            for entry in entries.values():
                entry.config(state="normal")
                entry.delete(0, END)
                entry.config(state="readonly")

            remaining_label.config(text="Remaining: ₹0")
            return

        if not value.isdigit():
            return

        amount = int(value)
        remaining = amount

        for note in notes:

            count = remaining // note
            remaining %= note

            entries[note].config(state="normal")
            entries[note].delete(0, END)
            entries[note].insert(0, count)
            entries[note].config(state="readonly")

        remaining_label.config(
            text=f"Remaining: ₹{remaining}"
        )

    amount_entry.bind("<KeyRelease>", calculator)


def msg():

    response = messagebox.askyesno(
        "Start",
        "Would you like to calculate denomination counts?"
    )

    if response:
        topwin()



Label(
    root,
    text="DENOMINATION COUNTER",
    font=("Segoe UI", 24, "bold"),
    bg="#6C63FF",
    fg="white"
).pack(pady=15)

Label(
    root,
    text="Count your currency notes instantly!",
    font=("Segoe UI", 12),
    bg="#6C63FF",
    fg="white"
).pack()

try:

    upload = Image.open("jjk.jpg")
    upload = upload.resize((320, 320))

    image = ImageTk.PhotoImage(upload)

    img_label = Label(root, image=image, bg="#6C63FF")
    img_label.image = image
    img_label.pack(pady=15)

except Exception:

    Label(
        root,
        text="Image not found",
        font=("Segoe UI", 14),
        bg="#6C63FF",
        fg="white"
    ).pack(pady=50)

Label(
    root,
    text="Welcome! Click below to calculate denominations.",
    font=("Segoe UI", 12),
    bg="#6C63FF",
    fg="white"
).pack(pady=10)

Button(
    root,
    text="Let's Get Started",
    command=msg,
    bg="#FF6B6B",
    fg="white",
    font=("Segoe UI", 13, "bold"),
    padx=20,
    pady=10,
    cursor="hand2"
).pack(pady=20)

root.mainloop()