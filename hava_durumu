import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def havani_eldeet(city):
    API_key = "fcb39de9ebeb0e3ae849f0de68229279"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("hatali", "sehir bulunamadi")
        return None

    hava = res.json()
    icon_id = hava["weather"][0]["icon"]
    hava_durumu = hava["main"]["temp"] - 273.15
    tanim = hava["weather"][0]["description"]
    sehir = hava["name"]
    ulke = hava["sys"]["country"]

    etiket_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return etiket_url, ulke, sehir, tanim, hava_durumu 

# havani aratmak
def aratma():
    city = sehir_dahilet.get()
    result = havani_eldeet(city)
    if result is None:
        return
    # egerki veriler dogruysa, verileri paketi ac
    etiket_url, ulke, sehir, tanim, hava_durumu = result
    konum_etiketi.configure(text=f"{sehir}, {ulke}")
    fotograf = Image.open(requests.get(etiket_url, stream=True).raw)
    icon = ImageTk.PhotoImage(fotograf)
    icon_label.configure(image=icon)
    icon_label.image = icon
    sicaklik_etiketi.configure(text=f"Hava durumu: {hava_durumu:.2f} °C")
    tanim_etiketi.configure(text=f"Tanım: {tanim}")

screen = ttkbootstrap.Window(themename="flatly")
screen.title("Hava uygulmasi")
screen.geometry("400x400")

# yazi tipi  ve arayuz uygulamasi
sehir_dahilet = ttkbootstrap.Entry(screen, font="Arial, 18")
sehir_dahilet.pack(pady=10)

# buton arayuzu
arama_butonu = ttkbootstrap.Button(screen, text="Search", command=aratma, bootstyle="warning C")
arama_butonu.pack(pady=10)

# sehir ve hava isimlerini gosterme
konum_etiketi = tk.Label(screen, font="Arial 23")
konum_etiketi.pack()

# hava arayuzu gosterme
sicaklik_etiketi = tk.Label(screen, font="Arial, 20")
sicaklik_etiketi.pack()

# hava durumun tanimi
tanim_etiketi = tk.Label(screen, font="Arial, 20")
tanim_etiketi.pack()

icon_label = tk.Label(screen)
icon_label.pack()

screen.mainloop()
