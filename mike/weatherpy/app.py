from datetime import datetime
import math

from Main import kToC, kToF, weatherGetFlask, degree

from flask import Flask, request
from flask import render_template

from Main import flaskbool

app = Flask(__name__)



@app.route('/bye')
def bye_world():
    return "bye"

@app.route('/pi')
def pi():
    return str(math.pi*1)

# @app.route("/index")
# def index():
#     return render_template("default.html", time=datetime.now())
@app.route('/weather')
def weather():
    zip = request.args.get('zip')
    country = request.args.get('country', 'us')
    if not zip or not country:
        return "Please input zip via adding \'?zip=(zip)\' to adress bar"
    output = weatherGetFlask(str(zip), str(country))
    temperatureC = str(kToC(output)) + degree() + "C"
    temperatureF = str(kToF(output)) + degree() + "F"
    temperature = str(output) + " Kelvin"
    return render_template("weather.html", weather = temperatureC, weatherF = temperatureF, weatherK = temperature)

if __name__ == '__main__':
    app.run(debug = True)