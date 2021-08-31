from tkinter import *

url = "api.openweathermap.org/data/2.5/weather?q={}&appid={}"

app = Tk()
app.title("weather app")
app.geometry("600x350")

def search():
    pass

city_text = StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

search_btn = Button(app, text="search weather ", width=13,command=search)
search_btn.pack()

location_lbl = Label(app, text="location",font =("bold",20))
location_lbl.pack()

image = Label(app,bitmap="image")
image.pack()


temp_lbl = Label(app, text ="temperature")
temp_lbl.pack()

weather_lbl = Label(app,text ="weather")
weather_lbl.pack()

app.mainloop()