from tkinter import *
from tkinter import ttk
import requests

def dataGet():
    city_Name = cityName.get()
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_Name}&appid={api.key}")
        data = response.json()
        
        if response.status_code == 200:
            weather_main = data["weather"][0]["main"]
            wLabel1.config(text=weather_main)
            wbLabel1.config(text=data["weather"][0]["description"])
            tempLabel1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
            pressureLabel1.config(text=str(data["main"]["pressure"]) + " hPa")
            
            if weather_main == "Clear":
                win.config(bg="orange")
            elif weather_main == "Rain":
                win.config(bg="blue")
            elif weather_main == "Clouds":
                win.config(bg="gray")
            elif weather_main == "Snow":
                win.config(bg="white")
            else:
                win.config(bg="pink")  # Default color
        else:
            wLabel1.config(text="N/A")
            wbLabel1.config(text="N/A")
            tempLabel1.config(text="N/A")
            pressureLabel1.config(text="N/A")
            win.config(bg="pink")  # Default color
    except KeyError as ke:
        wLabel1.config(text="Error")
        wbLabel1.config(text="Error")
        tempLabel1.config(text="Error")
        pressureLabel1.config(text="Error")
        win.config(bg="pink")  # Default color
    except Exception as e:
        wLabel1.config(text="Error")
        wbLabel1.config(text="Error")
        tempLabel1.config(text="Error")
        pressureLabel1.config(text="Error")
        win.config(bg="pink")  # Default color

win = Tk()
win.title("Weather App")
win.config(bg="pink")
win.geometry("500x500")


nameLabel = Label(win, text="Harshita ka", font=("Arial", 40, "bold"))
nameLabel.place(x=25, y=5, height=45, width=450)

nameLabel = Label(win, text="Weather App", font=("Arial", 40, "bold"))
nameLabel.place(x=25, y=50, height=50, width=450)

cityName = StringVar()
listName = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, text="Weather App", values=listName, font=("Arial", 20, "bold"), textvariable=cityName)
com.place(x=25, y=120, height=50, width=450)

wLabel = Label(win, text="Weather Climate", font=("Arial", 20))
wLabel.place(x=25, y=260, height=50, width=220)

wLabel1 = Label(win, text="", font=("Arial", 20))
wLabel1.place(x=260, y=260, height=50, width=220)

wbLabel = Label(win, text="Weather Description", font=("Arial", 18))
wbLabel.place(x=25, y=320, height=50, width=220)

wbLabel1 = Label(win, text="", font=("Arial", 18))
wbLabel1.place(x=260, y=320, height=50, width=220)

tempLabel = Label(win, text="Temperature", font=("Arial", 20))
tempLabel.place(x=25, y=380, height=50, width=220)

tempLabel1 = Label(win, text="", font=("Arial", 20))
tempLabel1.place(x=260, y=380, height=50, width=220)

pressureLabel = Label(win, text="Pressure", font=("Arial", 20))
pressureLabel.place(x=25, y=440, height=50, width=220)

pressureLabel1 = Label(win, text="", font=("Arial", 20))
pressureLabel1.place(x=260, y=440, height=50, width=220)

doneButton = Button(win, text="Done", font=("Arial", 20, "bold"), command=dataGet)
doneButton.place(x=200, y=190, height=50, width=100)

win.mainloop()
