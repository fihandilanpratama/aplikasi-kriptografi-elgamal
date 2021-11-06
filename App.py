from tkinter import *
from tkinter import messagebox
import functions

root = Tk()
root.title("Aplikasi Kriptografi Elgamal Sederhana")
# root.iconbitmap('@/home/fihan/code/aplikasi-kriptografi-elgamal/emblemencryptedlocked_93479.xbm')
root.geometry("760x600")

def btn_clear():
  response =  messagebox.askyesno("warning", "are you sure want to clear all fields ?")
  if response == 1:
    plaintextInput.delete(0, END)
    chipertextInput.delete(1.0, END)
    publicKeyY.delete(0, END)
    publicKeyG.delete(0, END)
    publicKeyP.delete(0, END)
    privateKeyX.delete(0, END)
    privateKeyP.delete(0, END)
    chipertextOutput.delete(1.0, END)
    privateKeyDecX.delete(0, END)
    privateKeyDecP.delete(0, END)
    plaintextOutput.delete(0, END)


pv = {}
def do_encrypt():
  plaintext = plaintextInput.get()
  if len(plaintext) == 0:
    messagebox.showinfo("information", "please fill in the plaintext first!")
    return
  global pv
  pv = functions.getPropertyValues()
  chipertext = functions.encryptPlaintext(plaintext, pv["p"], pv["g"], pv["y"])

  # tampilkan ke UI
  publicKeyY.insert(0, pv["y"])
  publicKeyG.insert(0, pv["g"])
  publicKeyP.insert(0, pv["p"])
  privateKeyX.insert(0, pv["x"])
  privateKeyP.insert(0, pv["p"])
  chipertextOutput.insert(1.0, chipertext)


def do_decrypt():
  chipertext = chipertextInput.get(1.0, END)
  x = privateKeyDecX.get()
  p = privateKeyDecP.get()
  if len(chipertext) == 1 or len(x) == 0 or len(p) == 0:
    messagebox.showinfo("information", "please fill in the chipertext, x, and p first!")
    return
  plaintext = functions.decryptChipertext(chipertext, x, p)
  plaintextOutput.insert(0, plaintext)


def do_copy():
  chipertext = chipertextOutput.get(1.0, END)
  x = privateKeyX.get()
  p = privateKeyP.get()
  chipertextInput.insert(1.0, chipertext)
  privateKeyDecX.insert(0, x)
  privateKeyDecP.insert(0, p)
  # root.clipboard_clear()
  # root.clipboard_append(chipertext)
  # root.update() # now it stays on the clipboard after the window is closed


# column1
column1 = LabelFrame(root,text="encrypt column", padx=5, pady=5)
column1.grid(row=0, column=0, padx=10, pady=10)

plaintextLabel = Label(column1, text="masukkan plaintext : ").grid(row=0, column=0, columnspan=6, pady=10)
plaintextInput = Entry(column1, width=40)
plaintextInput.grid(row=1, column=0, columnspan=6,  padx=10)
encryptButton = Button(column1, text="encrypt", command=do_encrypt).grid(row=2, column=0, columnspan=6, pady=5)

publicKeyLabel = Label(column1, text="public key : ").grid(row=3, column=0, columnspan=6, pady=10)
publicKeyYLabel = Label(column1, text="y = ").grid(row=4, column=0)
publicKeyGLabel = Label(column1, text="g = ").grid(row=4, column=2)
publicKeyPLabel = Label(column1, text="p = ").grid(row=4, column=4)
publicKeyY = Entry(column1, width=8)
publicKeyY.grid(row=4, column=1)
publicKeyG = Entry(column1, width=8)
publicKeyG.grid(row=4, column=3)
publicKeyP = Entry(column1, width=8)
publicKeyP.grid(row=4, column=5)

privateKeyLabel = Label(column1, text="private key : ").grid(row=5, column=0, columnspan=6, pady=10)
privateKeyXLabel = Label(column1, text="x = ").grid(row=6, column=0)
privateKeyPLabel = Label(column1, text="p = ").grid(row=6, column=2)
privateKeyX = Entry(column1, width=8)
privateKeyX.grid(row=6, column=1)
privateKeyP = Entry(column1, width=8)
privateKeyP.grid(row=6, column=3)

chipertextOutputLabel = Label(column1, text="chipertext : ").grid(row=7, column=0, columnspan=6, pady=15)
chipertextOutput = Text(column1, width=40, height=10)
chipertextOutput.grid(row=8, column=0, columnspan=6, pady=5)
copyButton = Button(column1, text="copy and paste to decrypt", command=do_copy).grid(row=9, column=0, columnspan=6, pady=3)

# column 2
column2 = LabelFrame(root,text="decrypt column", padx=5, pady=5)
column2.grid(row=0, column=1, padx=10, pady=10, sticky="n")

chipertextLabel = Label(column2, text="masukkan chipertext : ").grid(row=0, column=0, pady=10, columnspan=4)
chipertextInput = Text(column2, width=40, height=10)
chipertextInput.grid(row=1, column=0, padx=10, columnspan=4)
Label(column2, text="masukkan private key : ").grid(row=2, column=0, columnspan=4, pady=10)
Label(column2, text="x = ").grid(row=3, column=0)
privateKeyDecX = Entry(column2, width=8)
privateKeyDecX.grid(row=3, column=1)
Label(column2, text="p = ").grid(row=3, column=2)
privateKeyDecP = Entry(column2, width=8)
privateKeyDecP.grid(row=3, column=3, pady=5)
decryptButton = Button(column2, text="decrypt", command=do_decrypt).grid(row=4, column=0, columnspan=4, pady=10)

Label(column2, text="plaintext : ").grid(row=5, column=0, columnspan=4, pady=15)
plaintextOutput = Entry(column2, width=40)
plaintextOutput.grid(row=6, column=0, columnspan=4, pady=9)
Label(column2, text="\n\n\n").grid(row=7, column=0, columnspan=4)

Button(root, text="clear", width=30, command=btn_clear).grid(row=1, column=0, columnspan=2)


root.mainloop()