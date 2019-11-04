import tkinter as tk
from tkinter import *
import json
import urllib.request
import config

class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        #self.master.geometry('1000x500')

        top_side = tk.LabelFrame(self.master, text="Hi there:")
        down_side = tk.LabelFrame(self.master, text="Convert:", height=450, width=950)
        config_frame = tk.LabelFrame(down_side, text="Google API Key Config:", width=450)
        address_frame = tk.LabelFrame(down_side, text="Address to Lat/Lng")
        lat_lng_frame = tk.LabelFrame(down_side, text='Lat/Lng to Address', width=50)

        top_side.grid(row=0)
        down_side.grid(row=1)

        config_frame.grid(row=0, column=0, padx=(10, 10))
        lat_lng_frame.grid(row=1, column=0, padx=(10, 10))
        address_frame.grid(row=0, rowspan=2, column=1, padx=(10, 10),pady=(10, 10))

        self.google_api_key = tk.StringVar(value=config.Google_API_Key)
        self.google_api_key_input = Entry(config_frame, textvariable=self.google_api_key, width=50)
        self.google_api_key_lb = tk.Label(config_frame, text='Google API KEY')
        self.close = tk.Button(top_side, text='Exit', command=self.master.destroy)
        self.top_label = tk.Label(top_side, text="Welcome to use Address translator!!!")

        self.top_label.grid(row=0, column=0)
        self.close.grid(row=0, column=1)

        self.google_api_key_lb.grid(row=0, column=0)

        self.google_api_key_input.grid(row=0, column=1)

        self.add1_lb = tk.Label(address_frame, text='Address Line 1: ')
        self.add2_lb = tk.Label(address_frame, text='Address Line 2: ')
        self.city_lb = tk.Label(address_frame, text='City: ')
        self.state_lb = tk.Label(address_frame, text='State: ')
        self.country_lb = tk.Label(address_frame, text='Country: ')
        self.zip_code_lb = tk.Label(address_frame, text='Zip Code: ')

        self.add1_lb.grid(row=0, column=0, sticky='w')
        self.add2_lb.grid(row=1, column=0, sticky='w')
        self.city_lb.grid(row=2, column=0, sticky='w')
        self.state_lb.grid(row=3, column=0, sticky='w')
        self.country_lb.grid(row=4, column=0, sticky='w')
        self.zip_code_lb.grid(row=5, column=0, sticky='w')

        self.add1 = tk.StringVar()
        self.add2 = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.country = tk.StringVar()
        self.zip_code = tk.StringVar()

        self.input_lat_lb = tk.Label(lat_lng_frame, text='Lat: ')
        self.input_lng_lb = tk.Label(lat_lng_frame, text='Lng: ')
        self.input_lat_lb.grid(row=0, column=0, sticky='w')
        self.input_lng_lb.grid(row=1, column=0, sticky='w')

        self.input_lat = tk.StringVar(value="38.971500")
        self.input_lng = tk.StringVar(value="-76.940308")

        self.input_lat_entry = Entry(lat_lng_frame, textvariable=self.input_lat)
        self.input_lng_entry = Entry(lat_lng_frame, textvariable=self.input_lng)

        self.input_lat_entry.grid(row=0, column=1, sticky='w')
        self.input_lng_entry.grid(row=1, column=1, sticky='w')

        self.get_lat_lng = tk.Button(address_frame, text="Get Lat/Lng")
        self.get_address = tk.Button(lat_lng_frame, text='Get Address', command=self.geocode_to_address)
        self.get_lat_lng.grid(row=8, column=0, sticky='w')
        self.get_address.grid(row=2, column=0, sticky='w')

        self.address_to_lat_lng_result = tk.StringVar(value='SSS')
        self.get_address_result = tk.StringVar()

        self.get_lat_lng_entry = tk.Entry(address_frame, textvariable=self.address_to_lat_lng_result)
        self.get_address_entry = tk.Entry(lat_lng_frame, textvariable=self.get_address)
        self.get_lat_lng_entry.grid(row=8, column=1)
        self.get_address_entry.grid(row=2, column=1)

    def create_widgets(self):
        pass

    def address_to_geocode(self):
        pass

    def geocode_to_address(self):
        lat = self.input_lat.get()
        lng = self.input_lng.get()
        api_key = self.google_api_key.get()
        request = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}".format(lat=lat, lng=lng, api_key=api_key)
        with urllib.request.urlopen(request) as response:
            feedback = response.read()
        results = json.loads(feedback)
        print(results)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
