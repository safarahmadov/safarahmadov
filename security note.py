#security note

import tkinter
from PIL import Image, ImageTk
from cryptography.fer


#resim koyulma asamasi
screen=tkinter.Tk()
screen.title("security note")
screen.minsize(height=800, width=400)

picture = Image.open("C:/Users/safar/OneDrive/Masaüstü/zyro-image.png")
new_size=(100,100)
new_picutre=picture.resize(new_size)

images=ImageTk.PhotoImage(new_picutre)

image=tkinter.Label(screen, image=images)
image.pack()

title_text=tkinter.Label(text="Enter Your Title", font=("Arial", 14, "bold"))
title_text.pack(pady=20)


#entry
olusturma=tkinter.Entry(width=50)
olusturma.pack()

secret_text=tkinter.Label(text="Enter Your Secret", font=("Arial", 14, "bold"))
secret_text.pack(pady=20)

text=tkinter.Text(width=40, height=20)
text.pack()


key_label=tkinter.Label(text="Enter Master Key", font=("Arial", 14, "bold"))
key_label.pack(pady=10)



#def ad_olusturma():
 #   olusturma.config()


password=tkinter.Entry(screen, width=50)  #show="*")
password.pack(pady=10)


key=Fernet.generate_key()
sifrelenmis=Fernet(key)

sifreli_metin = None
orijinal_metin = None



def sifrele():
    global sifreli_metin, key
    password2=password.get()

    dosya_adi=olusturma.get()+".txt"
    
    metin = text.get("1.0", tkinter.END)
    sifreli_metin = sifrelenmis.encrypt(metin.encode())
    
    with open(dosya_adi, "wb") as dosya:
        dosya.write(sifreli_metin)
    password1=sifrelenmis.encrypt(password2.encode())

def coz():
    global orijinal_metin, key
    password2=password.get()
    dosya_adi=olusturma.get()+".txt"
    
    orijinal_metin = sifrelenmis.decrypt(sifreli_metin).decode()
    password1=sifrelenmis.encrypt(password2.encode()).decode()
    with open(dosya_adi, "w") as dosya:
      
        #sifreli_metin = dosya.read()
        dosya.write(orijinal_metin)
        
        


button=tkinter.Button(text="Save & Encrypt", width=20, command=sifrele)
button.pack(pady=10)


button=tkinter.Button(text="Decrypt", width=20, command=coz )
button.pack(pady=10)
tkinter.mainloop()
