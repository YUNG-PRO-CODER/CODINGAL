from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinter import simpledialog

win = Tk()
win.title("My Photo Album")
win.geometry("400x350")
title = Label(win, text="My Photo Album", fg="white", bg="blue", width=40)
title.pack(pady=8)
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
)

if image_path:
    img_file = Image.open(image_path)
    img_file = img_file.resize((350, 110))
    ph = ImageTk.PhotoImage(img_file)
    pic = Label(win, image=ph)
    pic.image = ph
    pic.pack(pady=8)

    def show_message():
        messagebox.showinfo("Good!", "You selected the photo.")

    def show_details():
        tp = Toplevel(win)
        tp.title("Details")
        tp.geometry("250x100")
        location = simpledialog.askstring("Photo Location", "Type the location of your photo:")

        if location:
            info = Label(tp, text=f"Location: {location}")
            info.pack(pady=20)

    message_btn = Button(win, text="Click to React", fg="blue", bg="purple", command=show_message)
    message_btn.pack(pady=8)
    details_btn = Button(win, text="View Details", bg="yellow", fg="green", command=show_details)
    details_btn.pack(pady=8)
else:
    Label(win, text="No image selected.").pack(pady=20)

win.mainloop()