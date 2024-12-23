from flask import Flask, render_template
import pandas as pd
from pathlib import Path

'''
Notes
images need to be in the folder static
html pages need to be in the folder templates
'''

'''
best to use __name__ here - name takes on the value of the script executing
unless it's being run itslef then __name__ == __main__
'''
app=Flask("__name__")

stations = pd.read_csv('../data_sm/stations.txt', skiprows=17)
stations = stations[["STAID","STANAME                                 ","CN"]].to_html()


# http://127.0.0.1:5000/home
@app.route("/")
def home():

    '''
    stations gets sent to the html page in the return statement
    you must have the 'safe' keyword to render the table in hte html template
    this line goes in the html template
    <p> {{stations|safe}}</p>
    '''
    return render_template("home.html", stations=stations)

app.route("/api/v1/<word>")
def word(word):
    return {"word": word}

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filepath = Path('\\Users\\Tony\\GitHub\\data_sm\\')
    station_id = str(station).zfill(6)
    print (f"TG_STAID{station_id}.txt")
    filename = (str(filepath) + '\\' + f"TG_STAID{station_id}.txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    celcius = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    farenheight = (celcius*9/5)+32
    return {"station": station,
            "date": date,
            "Temp. Celcius": celcius,
            "Temp. Farenheight": farenheight}
    #return render_template("about.html")


if __name__ == "__main__":
    # using different ports allows multiple Flask Apps 
    # to be run at the same time on different ports
    app.run(debug=True, port=5000)