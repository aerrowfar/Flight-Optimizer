from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,IntegerField, ValidationError, validators
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange, length
from wtforms.fields.html5 import DateField

class RegisterForm(FlaskForm):
    home_location = StringField("Departure Airport Code", validators=[DataRequired(), length(min=2,max=15)])
    earliest_dep_date = DateField("Earliest Departure Date (YYYY-MM-DD)", validators= [DataRequired()])
    latest_dep_date = DateField("Latest Departure Date (YYYY-MM-DD)", validators= [DataRequired()])
    latest_return_date = DateField("Latest Return Date (YYYY-MM-DD)", validators= [DataRequired()])
    des1 = StringField("First Destination Airport Code", validators=[DataRequired(), length(min=2,max=15)])
    min_stay1 = IntegerField("Minimum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    max_stay1 = IntegerField("Maximum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    des2 = StringField("Second Destination Airport Code", validators=[DataRequired(), length(min=2,max=15)])
    min_stay2 = IntegerField("Minimum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    max_stay2 = IntegerField("Maximum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    des3 = StringField("Third Destination Airport Code", validators=[DataRequired(), length(min=2,max=15)])
    min_stay3 = IntegerField("Minimum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    max_stay3 = IntegerField("Maximum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    des4 = StringField("Fourth Destination Airport Code", validators=[DataRequired(), length(min=2,max=15)])
    min_stay4 = IntegerField("Minimum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    max_stay4 = IntegerField("Maximum number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])

    submit = SubmitField("Generate")


#Class that encapsulates all the information needed to calculate the optimal set of flights
#Homelocation: The code for the airport that the person is coming from and returning to (String)
#earliestStart: The earliest possible time the first flight can be (datetime)
#latestStart: The latest possible time that the first flight can be (datetime)
#latestReturn: The latest possible time that the final flight can be (datetime)
class Trip:
  def __init__(self, homeLocation, earliestStart, latestStart, latestReturn):
    self.homeLocation = homeLocation
    self.earliestStart = earliestStart
    self.latestStart = latestStart
    self.latestReturn = latestReturn
    self.locations = []

  def addLocation(self, location):
    self.locations.append(location)
  
  def getLocations(self):
    return self.locations

  def getEarliestStart(self):
    return self.earliestStart

  def getLatestStart(self):
    return self.latestStart

  def getLatestReturn(self):
    return self.latestReturn

  def getHomeLocation(self):
    return self.homeLocation

#Class that encalpsulates the information about a single destination
#locationName: The name of the location, doesn't actually do anything but could be useful (String)
#airportCode: The airport code for this location (String)
#minStayLength: The minimum amount of time between arriving and leaving this location (String)
#maxStayLength: The maxiumum amount of time between arriving and leaving this location (String)
class Location:
  #Min and max stay length are in days
  def __init__(self, locationName, airportCode, minStayLength, maxStayLength):
    self.locationName = locationName
    self.airportCode = airportCode
    self.minStayLength = minStayLength
    self.maxStayLength = maxStayLength

  def getMinStayLength(self):
    return self.minStayLength
  
  def getMaxStayLength(self):
    return self.maxStayLength

  def getLocationName(self):
    return self.locationName
  
  def getAirportCode(self):
    return self.airportCode