from flask import Flask, render_template

'''
Notes
images need to be in the folder static
html pages need to be in the folder templates
'''

app=Flask("Website")

# http://127.0.0.1:5000/home
@app.route("/home")
def home():

    return render_template("flask_tutorial.html")

# http://127.0.0.1:5000/about
@app.route("/about/")
def about():

    return render_template("about.html")

app.run(debug=True)