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

        top_side = tk.LabelFrame(self.master, text="Hi there:", height=450, width=950)
        down_side = tk.LabelFrame(self.master, text="Convert:", height=450, width=950)
        config_frame = tk.LabelFrame(down_side, text="Google API Key Config:", width=450)
        address_frame = tk.LabelFrame(down_side, text="Address to Lat/Lng")
        lat_lng_frame = tk.LabelFrame(down_side, text='Lat/Lng to Address', width=450)

        top_side.grid(row=0)
        down_side.grid(row=1)

        config_frame.grid(row=0, column=0, padx=(10, 10))
        lat_lng_frame.grid(row=1, column=0, padx=(10, 10))
        address_frame.grid(row=0, rowspan=2, column=1, padx=(10, 10),pady=(10, 10))

        self.google_api_key = tk.StringVar()
        self.google_api_key.set(value=config.Google_API_Key)
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

        self.input_add1 = Entry(address_frame, textvariable=self.add1)
        self.input_add2 = Entry(address_frame, textvariable=self.add2)
        self.input_city = Entry(address_frame, textvariable=self.city)
        self.input_state = Entry(address_frame, textvariable=self.state)
        self.input_country = Entry(address_frame, textvariable=self.country)
        self.input_zip_code = Entry(address_frame, textvariable=self.zip_code)

        self.input_add1.grid(row=0, column=1, sticky='e')
        self.input_add2.grid(row=1, column=1, sticky='e')
        self.input_city.grid(row=2, column=1, sticky='e')
        self.input_state.grid(row=3, column=1, sticky='e')
        self.input_country.grid(row=4, column=1, sticky='e')
        self.input_zip_code.grid(row=5, column=1, sticky='e')

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

        self.get_lat_lng = tk.Button(address_frame, text="Get Lat/Lng", command=self.address_to_geocode)
        self.get_address = tk.Button(lat_lng_frame, text='Get Address', command=self.geocode_to_address)
        self.get_lat_lng.grid(row=8, column=0, sticky='w')
        self.get_address.grid(row=2, column=0, sticky='w')

        self.get_lat_lng_result = tk.StringVar()
        self.get_address_result = tk.StringVar()

        self.get_lat_lng_entry = tk.Entry(address_frame, textvariable=self.get_lat_lng_result)
        self.get_address_entry = tk.Entry(lat_lng_frame, textvariable=self.get_address_result)
        self.get_lat_lng_entry.grid(row=8, column=1)
        self.get_address_entry.grid(row=2, column=1)

    def create_widgets(self):
        pass

    def address_to_geocode(self):
        api_key = self.google_api_key.get()
        add1 = self.add1.get()
        add2 = self.add2.get()
        city = self.city.get()
        state = self.state.get()
        country = self.country.get()
        zip_code = self.zip_code.get()
        address_full_str=''
        address_full_list = [add1, add2, city, state, country, zip_code]
        for item in address_full_list:
            if item != '':
                address_full_str += (" " + item)
        address_full_str = address_full_str.replace(" ", "%20")
        #print(address_full_str)
        url_string = "https://maps.googleapis.com/maps/api/geocode/json?address=" \
                     "{place_text}&key={google_api_key}".format(place_text=address_full_str, google_api_key=api_key)
        print(url_string)
        with urllib.request.urlopen(url_string) as response:
            feedback = response.read()
        results = json.loads(feedback)
        if results['status'] != 'OK':
            self.get_lat_lng_result.set(value=str(results.get('status')))
            print(results.get('status'))
        else:
            lat_lng = results['results'][0]['geometry']['location']
        # print(lat_lng)
        # print(str(lat_lng))
            self.get_lat_lng_result.set(value=str(lat_lng))

    def geocode_to_address(self):
        lat = self.input_lat.get()
        lng = self.input_lng.get()
        api_key = self.google_api_key.get()
        url_string = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}".format(lat=lat, lng=lng, api_key=api_key)
        #print(url_string)
        with urllib.request.urlopen(url_string) as response:
            feedback = response.read()
        results = json.loads(feedback)
        best_match = results['results'][0]["formatted_address"]
        #print(best_match)
        self.get_address_result.set(value=best_match)
        self.update()
        #print(results)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
