from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import Flight,Route
from application.form import RegisterForm

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])

def index():
    form = RegisterForm ()
    if form.validate_on_submit():
        #these are all the variables collected from the input page. des for Destination and dur for Duration.
        dep_city = form.dep_city.data
        dep_date = form.dep_date.data
        des1 = form.des1.data
        dur1 = form.dur1.data
        des2 = form.des2.data
        dur2 = form.dur2.data
        des3 = form.des3.data
        dur3 = form.dur3.data
        des4 = form.des4.data
        dur4 = form.dur4.data

        flight = Flight(dep_city = dep_city,dep_date = dep_date, des1 = des1, dur1 = dur1, des2 = des2, dur2 = dur2, des3 = des3, dur3 = dur3,des4 = des4, dur4 = dur4)
        flight.save()
       
        #or backend functions can go here instead. 

        return redirect ("/results")
    return render_template("index.html", title = "Desired Itinery", form =form) 


@app.route("/aboutus")

def aboutus():
    #we can fill this out with whatever. 
    return render_template("aboutus.html") 


@app.route("/results")

def results():
    #so when you click generate, it comes here to display flights. Currently it just displays whatever you put in 
    #to the database from last step. 

    #back end functions can either go here. 
    flights = Flight.objects.order_by("dep_date")
    return render_template("results.html", flights = flights)

@app.route("/purchase", methods = ["GET","POST"])
#when you click on purchase, it takes the user to this function here.
def purchase():
    id = request.form.get('flightID')
    return render_template("purchase.html", id = id)