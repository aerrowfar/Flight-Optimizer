from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import Flight,Route, dbtrip, TripDoc
from application.form import RegisterForm, Trip, Location
from application import api


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])

def index():
    form = RegisterForm ()
    if form.validate_on_submit():
        #these are all the variables collected from the input page. 
        homeLocation = form.home_location.data
        earliestStart = form.earliest_dep_date.data
        latestStart = form.latest_dep_date.data
        latestReturn = form.latest_return_date.data
        des1 = form.des1.data
        min_stay1 = form.min_stay1.data
        max_stay1 = form.max_stay1.data
        des2 = form.des2.data
        min_stay2 = form.min_stay2.data
        max_stay2 = form.max_stay2.data
        des3 = form.des3.data
        min_stay3 = form.min_stay3.data
        max_stay3 = form.max_stay3.data
        des4 = form.des4.data
        min_stay4 = form.min_stay4.data
        max_stay4 = form.max_stay4.data

       

        #here we save all the variables to the database.
        trip = dbtrip(homeLocation=homeLocation,earliestStart = earliestStart,latestStart = latestStart,latestReturn=latestReturn,des1=des1,min_stay1=min_stay1,max_stay1=max_stay1,des2=des2,min_stay2=min_stay2,max_stay2=max_stay2,des3=des3, min_stay3=min_stay3,max_stay3=max_stay3,des4=des4,min_stay4=min_stay4,max_stay4=max_stay4)
        trip.save()
        
        return redirect ("/results")
        
    return render_template("index.html", title = "Desired Itinery", form =form) 


@app.route("/aboutus")

def aboutus():
    #we can fill this out with whatever. 
    return render_template("aboutus.html") 


@app.route("/results")

def results():
    #you come here from the landing page.
   
    #here we load the first save in the database collection.
    info = dbtrip.objects.first()

    #we dig out all the variables again.
    homeLocation = info.homeLocation
    earliestStart = info.earliestStart
    latestStart = info.latestStart
    latestReturn = info.latestReturn
    des1 = info.des1
    min_stay1 = info.min_stay1
    max_stay1 = info.max_stay1
    des2 = info.des2
    min_stay2 = info.min_stay2
    max_stay2 = info.max_stay2
    des3 = info.des3
    min_stay3 = info.min_stay3
    max_stay3 = info.max_stay3
    des4 = info.des4
    min_stay4 = info.min_stay4
    max_stay4 = info.max_stay4

    #here we set the Trip object with all the collected variables.
    trip = Trip(homeLocation, earliestStart, latestStart, latestReturn)
    Location_1 = Location("",des1,min_stay1,max_stay1)
    Location_2 = Location("",des2,min_stay2,max_stay2)
    Location_3 = Location("",des3,min_stay3,max_stay3)
    Location_4 = Location("",des4,min_stay4,max_stay4)

    trip.addLocation(Location_1)
    trip.addLocation(Location_2)
    trip.addLocation(Location_3)
    trip.addLocation(Location_4)

    #calling API with the collected objects.
    flights = api.getMinRoute(trip)

    
    return render_template("results.html", flights = flights)

@app.route("/purchase", methods = ["GET","POST"])
#when you click on purchase, it takes the user to this function here.
def purchase():
    id = request.form.get('flightID')
    return render_template("purchase.html", id = id)