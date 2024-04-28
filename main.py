
from data_process import Weather_data
from flask import Blueprint,render_template,redirect,request



main = Blueprint('main',__name__)
@main.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form.get("city_name")
        data =  Weather_data(city)
        weather = data.weather_data()
        temperature = data.weather_tempreature()
        wind = data.weather_wind()
        name = data.name_city()
        time = data.time()
        return render_template("home.html", weather=weather,
                               temperature=temperature,
                               wind=wind,
                               method=True,
                               time=time,
                               name=name)
    return render_template("home.html")

@main.route('/current_location')
def current_location():
    loc = Weather_data.current_location()
    data = Weather_data(loc)
    weather = data.weather_data()
    temperature = data.weather_tempreature()
    wind = data.weather_wind()
    name = data.name_city()
    time = data.time()
    return render_template("home.html", weather=weather,
                           temperature=temperature,
                           wind=wind,
                           method=True,
                           time=time,
                           name=name)

