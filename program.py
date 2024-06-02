from tkinter import *
import os
import base64
from PIL import Image, ImageTk

def clear():
    os.system("clear")
    
def program_exit():
    program.destroy()
    print("Clicked button and exited the program.")

def save_encrypt():
    l3 = Label(program, text="")
    
    text1 = e1.get()
    text2 = t1.get("1.0","end-1c")

    text = text1 + " " + text2
    encrypted_text = text
    encrypted_text_bytes = encrypted_text.encode("ascii")
    encrypt_base64 = base64.b64encode(encrypted_text_bytes)
    encrypt_base64_string = encrypt_base64.decode("ascii")
    
    f = open("crypto.txt","a")
    f.write(str(encrypt_base64_string))
    f.write("\n")
    f.close()
    
    l3.after(5000, lambda: l3.destroy())
    l3 = Label(program, text="Encrypted message is writed another file.", font=("tahoma",15,"normal"))
    l3.pack()

def decrypt():
    l3 = Label(program, text="")
    text3 = e2.get()
    decrypt_base64 = text3
    decrypt_base64_bytes = decrypt_base64.encode("ascii")
    
    string_message_bytes = base64.b64decode(decrypt_base64_bytes)
    string_message = string_message_bytes.decode("ascii")
    
    f = open("decrypto.txt","a")
    f.write(f"Sifre: {text3}\nSifrenin Anlami: {string_message}\n")
    f.write("\n")
    f.close()
    
    l4 = Label(program, text="")
    l3.after(5000, lambda: l3.destroy())
    l3 = Label(program, text=f"{string_message}", font=("tahoma",15,"normal"))
    l3.pack()
    l4.after(3500, lambda: l4.destroy())
    l4 = Label(program, text="Mesajin çozumu bir dosyaya kayit edip yazilmistir.", font=("tahoma",15,"normal"))
    l4.pack()
    
clear()
program = Tk()
program.geometry("400x800")
program.title("Secret Notes")
# Image
img = Image.open("pictures/OIP-2378218113.jpeg")
resize_img = img.resize((165,140))
img2 = ImageTk.PhotoImage(resize_img)
img_lbl = Label(image=img2)
img_lbl.image = img2
img_lbl.pack()

l1 = Label(program, text="Enter Your Title", font=("tahoma",15,"normal"))
l1.pack()
e1 = Entry(program, width=30)
e1.pack()

l2 = Label(program, text="Enter Your Secret", font=("tahoma",15,"normal"))
l2.pack()
t1 = Text(program, width=45, height=40)
t1.pack()

l3 = Label(program, text="Enter Master Key", font=("tahoma",15,"normal"))
l3.pack()
e2 = Entry(program, width=30)
e2.pack()

b1 = Button(program, text="Save & Encrypt", font=("tahoma",15,"normal"), command=save_encrypt)
b1.pack()
b2 = Button(program, text="Decrypt", font=("tahoma", 15, "normal"), command=decrypt)
b2.pack()
b3 = Button(program, text="Quit", fg="white", bg="dark red", font=("tahoma",15,"normal"), command=program_exit)
b3.pack()

program.mainloop()
