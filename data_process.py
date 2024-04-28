
class Weather_data:
    import requests
    def __init__(self,city:str):
        self.apikey='fd0401d86ff59b82a9120ebad3b0ce8c'
        self.city = city
        self.lat,self.lon = self.get_lat_lon()
        self.weatherdata = self.get_weather_data()
    
    def get_lat_lon(self):
        self.place = self.requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=5&appid={self.apikey}").json()[0]
        lat = self.place['lat']
        lon = self.place['lon']
        return lat,lon
    
    def get_weather_data(self):
        self.wheather_api = self.requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.apikey}").json()
        return self.wheather_api


    def weather_data(self):
        return self.weatherdata['weather'][0]
    
    def weather_tempreature(self):
        temp = self.weatherdata['main']
        celsius = "{data:.2f}".format(data =temp['temp'] - 274.15)
        feels_like = "{data:.2f}".format(data =temp['temp'] - 274.15)
        humidity = f"{temp['humidity']}%"
        return {'temp':celsius,"feels_like":feels_like,"humidity":humidity,'feels_like':feels_like}

    def weather_wind(self):
        wind = self.weatherdata['wind']
        wind_speed = "{data:.2f}km/h".format(data = wind['speed'] * 3.6)
        return {"wind_speed":wind_speed}


    def name_city(self):
        try:
            return f"{self.place['name']} {self.place['state']} {self.place['country']}  {self.place['local_names']['kn']}"
        except Exception as error:
            return f"{self.place['name']} {self.place['state']} {self.place['country']}"

    def time(self):
        import datetime as dt
        formates = dt.datetime.utcfromtimestamp(self.wheather_api['dt'] + self.wheather_api['timezone'])
        return formates.strftime("%b %d %I:%M, %p")
    @staticmethod
    def current_location():
        import geocoder
        current_loc = geocoder.ip('me')
        return  current_loc.geojson['features'][0]['properties']['city']
