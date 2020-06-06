import flask
from application import db


class Flight(db.Document):
    dep_date = db.DateTimeField()
    dep_city = db.StringField( max_length=50)
    des1 = db.StringField (max_length=50)
    dur1 = db.IntField (max_length = 3)
    des2 = db.StringField (max_length=50)
    dur2 = db.IntField (max_length = 3)
    des3 = db.StringField (max_length=50)
    dur3 = db.IntField (max_length = 3)
    des4 = db.StringField (max_length=50)
    dur4 = db.IntField (max_length = 3)

class Route(db.Document):
    dep_date= db.DateTimeField()
    land_date= db.DateTimeField()
    carrier = db.StringField()
    flightId = db.IntField()
    cost = db.IntField()

class dbtrip(db.Document):
    homeLocation = db.StringField()
    earliestStart = db.DateTimeField()
    latestStart = db.DateTimeField()
    latestReturn = db.DateTimeField()
    des1 = db.StringField()
    min_stay1 = db.IntField()
    max_stay1 = db.IntField()
    des2 = db.StringField()
    min_stay2 = db.IntField()
    max_stay2 = db.IntField()
    des3 = db.StringField()
    min_stay3 = db.IntField()
    max_stay3 = db.IntField()
    des4 = db.StringField()
    min_stay4 = db.IntField()
    max_stay4 = db.IntField()

class TripDoc (db.DynamicDocument):
    pass