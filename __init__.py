from flask import Flask
from main import main as Main
def wheather_api ():
    app = Flask(__name__)
    app.register_blueprint(Main)
    return  app
if __name__ ==  "__main__":
    wheather_api().run(debug=True)

