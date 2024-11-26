from flask import Flask, render_template
import pandas as pd

'''
Notes
images need to be in the folder static
html pages need to be in the folder templates
'''

# best to use __name__ here - name takes on the value of the script executing
# unless it's being run itslef then __name__ == __main__
app=Flask("__name__")

# http://127.0.0.1:5000/home
@app.route("/")
def home():

    return render_template("home.html")

# http://127.0.0.1:5000/about
@app.route("/api/v1/<station>/<data>")
def about(station, date):
    df = pd.read_csv("")
    temprature = df.station(date)
    return {"sation": station,
            "date": date,
            "temprature": temprature}
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)