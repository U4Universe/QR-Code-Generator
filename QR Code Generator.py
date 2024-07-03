import qrcode
from qrcode import QRCode
from tkinter import Tk, Button, Entry, Label, filedialog
from PIL import ImageTk, Image


#function to generate QR code
def generate_qr_code():
    data = entry.get()
    if data:
      qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 15,
        border = 7,
       )
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "#273746", back_color = "#FBFCFC")

    #saving the QR code in the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*png")])

    if file_path:
        img.save(file_path)
        show_qr(file_path)

#function to show the generated QR code in tkinter GUI
def show_qr(file_path):
    img = Image.open(file_path)
    img = img.resize((200, 200),Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img


#creating a GUI Window
root = Tk()
root.title("QR CODE GENERATOR")

#creating input box for data entry
Label(root, text="Enter the link: ").pack(pady = 5)
entry = Entry(root, width=50)
entry.pack(pady = 5)

#creating a submit button for output
Button(root, text="Generate QR Code", command=generate_qr_code).pack(pady=10)

#Label to display the generated QR
qr_label = Label(root)
qr_label.pack(pady = 10)

#starting the GUI loop
root.mainloop()


        

    
    
