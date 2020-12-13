# NOT WRITTEN BY ME, API.PY IS THE WORK OF MY CLASSMATE. IM INCLUDING ONLY FOR SAKE OF COMPLETION. 

import requests
import json
import time
import datetime
import dateutil.relativedelta as rd # https://stackoverflow.com/questions/35066588/is-there-a-simple-way-to-increment-a-datetime-object-one-month-in-python/35067328
from dijkstar import Graph, find_path

headers = {# headers for api queries 
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "5e68c96b41mshc14b96ebcb640f5p1a6a44jsn3fc5d81a8b37"
    }

#This is a helper method. You probably shouldn't be using it
#Returns a list with two elements. THe first element is the cost of all the flights, the second element is a list of the times for each flight
#data - the data object in getMinRoute()
#trip - the trip object for this trip
def getMinFlights(data, trip):
  graph = Graph()
  #Home->loc0
  for i in range(len(data[0])):
    for j in range(len(data[0][i]["Quotes"])):
      if(trip.getEarliestStart() <=datetime.datetime.strptime(data[0][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00")):#First flight not before earliest start
        if(trip.getLatestStart() >= datetime.datetime.strptime(data[0][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00")):#First flight not after latest start
          graph.add_edge(0,(0,i,j), data[0][i]["Quotes"][j]["MinPrice"])
  #loc->loc
  for m in range(len(data)-2):
    for i in range(len(data[m+1])):
      for j in range(len(data[m+1][i]["Quotes"])):
        for k0 in range(len(data[m])):
          for k1 in range(len(data[m][k0]["Quotes"])):
            if(datetime.datetime.strptime(data[m+1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") >= datetime.datetime.strptime(data[m][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") + datetime.timedelta(days=+trip.getLocations()[m].getMinStayLength())): #Ensures that the person remains at destination 0 for at least the min stay length         
              if(datetime.datetime.strptime(data[m+1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") <= datetime.datetime.strptime(data[m][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") + datetime.timedelta(days=+trip.getLocations()[m].getMaxStayLength())):#Ensures that the person remains at destination 0 for at most the max stay length
                if(datetime.datetime.strptime(data[m+1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") > datetime.datetime.strptime(data[m][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00")): #Correct chronology
                  graph.add_edge((m,k0,k1),(m+1,i,j), data[m+1][i]["Quotes"][j]["MinPrice"])
  #locN->home
  for i in range(len(data[len(data)-1])):
    for j in range(len(data[len(data)-1][i]["Quotes"])):
      for k0 in range(len(data[len(data)-2])):
        for k1 in range(len(data[len(data)-2][k0]["Quotes"])):
          if(datetime.datetime.strptime(data[len(data)-1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") >= datetime.datetime.strptime(data[len(data)-2][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") + datetime.timedelta(days=+trip.getLocations()[len(data)-2].getMinStayLength())): #Ensures that the person remains at destination 2 for at least the min stay length         
            if(datetime.datetime.strptime(data[len(data)-1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") <= datetime.datetime.strptime(data[len(data)-2][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") + datetime.timedelta(days=+trip.getLocations()[len(data)-2].getMaxStayLength())):#Ensures that the person remains at destination 2 for at most the max stay length
              if(datetime.datetime.strptime(data[len(data)-1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") > datetime.datetime.strptime(data[len(data)-2][k0]["Quotes"][k1]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00")): #Correct chronology
                if(datetime.datetime.strptime(data[len(data)-1][i]["Quotes"][j]["OutboundLeg"]["DepartureDate"], "%Y-%m-%dT00:00:00") <= trip.getLatestReturn()): # Last flight is before latest return date
                  graph.add_edge((len(data)-2,k0,k1),(len(data)-1,i,j), data[len(data)-1][i]["Quotes"][j]["MinPrice"])
      graph.add_edge((len(data)-1,i,j), 1, 0)
      
  path = find_path(graph, 0, 1)
  #print(path)
  flights = []
  for i in range(len(data)):
    
    flight = [] #each fight is an array for easy access
    #Carrier = ""
    #Destination = ""
    #Origin = "" 
    #print(data)

    # finds the carrier of each flight (using the carrier id) and adds the name to flight array
    for p in data[i][path[0][i+1][1]]["Carriers"]:
      if (p["CarrierId"] == data[i][path[0][i+1][1]]["Quotes"][path[0][i+1][2]]["OutboundLeg"]['CarrierIds'][0]):
        Carrier = "Carrier :" + p['Name']
    flight.append(Carrier)

    # finds the Origin of each flight (using the Origin id) and adds the name to flight array
    for p in data[i][path[0][i+1][1]]["Places"]:
      if (p['PlaceId'] == data[i][path[0][i+1][1]]["Quotes"][path[0][i+1][2]]["OutboundLeg"]['OriginId']):
        Origin = "Origin :" + p['Name']
    flight.append(Origin)  

    # finds the Destination of each flight (using the destination id) and adds the name to flight array
    for p in data[i][path[0][i+1][1]]["Places"]:
      if (p['PlaceId'] == data[i][path[0][i+1][1]]["Quotes"][path[0][i+1][2]]["OutboundLeg"]['DestinationId']):
        Destination = "Destination :" + p['Name']
    flight.append(Destination)    

    flight.append(data[i][path[0][i+1][1]]["Quotes"][path[0][i+1][2]]["OutboundLeg"]["DepartureDate"])#adds the departue date to the flight array

    flights.append(flight)#adds the (single) flight array to the flights array

  minFlights = [path[3], flights]
  return minFlights

#Returns a list. The first element of the list is the total cost. The second element is a list of departure dates
#trip - the trip object for this trip
def getMinRoute(trip, urlhost="GB/", urlcurrency="GBP/", urllang="en-GB/"):
  urlbase = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"
  locations = trip.getLocations()
  data = []

  if(len(locations) > 5 ):
    raise Exception("Too many locations")

  #home->loc0 
  data.append([])
  startDate = trip.earliestStart
  endDate = trip.latestStart
  while(1):
    urltakeoff = trip.getHomeLocation() + "/" #The origin place (see places)
    urldest = locations[0].airportCode + "/" #The destination place (see places)
    urldate = datetime.datetime.strftime(startDate, "%Y-%m") + "/" #The outbound date. Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”.
    superurl = urlbase + urlhost + urlcurrency + urllang + urltakeoff + urldest + urldate
    #print(superurl)
    querystring = {}

    response = requests.request("GET", superurl, headers=headers, params=querystring)

    #print(response.text) #print the raw text of the response
    jsonobj = response.json() #of type dict
    # type(jsonobj) #dict
    data[0].append(json.loads(response.text))
    if startDate > endDate or startDate > trip.getLatestReturn():
      break
    startDate+=rd.relativedelta(months=+1)
    
    
  #print("Locations: ", len(locations))

  i = 0
  #loc0->loc1->loc2->loc3->loc4
  while i < len(locations)-1:
    #print("Location: ", i)
    data.append([])
    startDate = trip.getEarliestStart()
    endDate = trip.getLatestStart()

    for j in range(i):
      startDate += datetime.timedelta(days=+locations[j].getMinStayLength())
      endDate += datetime.timedelta(days=+locations[j].getMaxStayLength())

    while(1):
      urltakeoff = locations[i].getAirportCode() #The origin place (see places)
      urldest = locations[i+1].getAirportCode() #The destination place (see places)
      urldate = datetime.datetime.strftime(startDate, "%Y-%m") #The outbound date. Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”.
      superurl = urlbase + urlhost + urlcurrency + urllang + urltakeoff +"/"+ urldest +"/"+ urldate
      #print(superurl)
      querystring = {}
      response = requests.request("GET", superurl, headers=headers, params=querystring)
      #print(response.text) #print the raw text of the response
      data[i+1].append(json.loads(response.text))
      if startDate > endDate or startDate > trip.getLatestReturn():
        break
      startDate+=rd.relativedelta(months=+1)
    i+=1

  #loc4->home
  data.append([])
  #print("Loc4->Home")
  startDate = trip.earliestStart
  endDate = trip.latestStart
  while i >=0:
    startDate += datetime.timedelta(days=+locations[i].getMinStayLength())
    endDate += datetime.timedelta(days=+locations[i].getMaxStayLength())
    i -= 1
  while(1):
    urltakeoff = locations[len(locations)-1].getAirportCode() + "/" #The origin place (see places)
    urldest = trip.getHomeLocation() + "/" #The destination place (see places)
    urldate = datetime.datetime.strftime(startDate, "%Y-%m") + "/" #The outbound date. Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”.
    superurl = urlbase + urlhost + urlcurrency + urllang + urltakeoff + urldest + urldate
    #print(superurl)
    querystring = {}
    response = requests.request("GET", superurl, headers=headers, params=querystring)
    #print(response.text) #print the raw text of the response
    data[len(locations)].append(json.loads(response.text))
    if startDate > endDate or startDate > trip.getLatestReturn():
      break
    startDate+=rd.relativedelta(months=+1)    

  #print(len(data))
  #print(data)

  return getMinFlights(data, trip)