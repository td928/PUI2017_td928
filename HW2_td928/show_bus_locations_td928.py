from __future__ import print_function
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# locate within the JSON file where all vehicles information is stored and find out how many vehicles 
# are currently operating
    
all_vehicles_info = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

vehicle_count = len(all_vehicles_info)

# print out bus line and number of operating vahicles

print('Bus Line : ' + sys.argv[2])
print('Number of Active Buses : ' + str(vehicle_count))

# print out the coordinate location for each individual vehicles

for i in range(vehicle_count):
    location = all_vehicles_info[i]['MonitoredVehicleJourney']['VehicleLocation']
    print ('Bus ' + str(i) + ' is at latitude ' + str(location['Latitude']) + ' and longitude ' + str(location['Longitude']))      

