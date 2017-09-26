from __future__ import print_function
import os
import sys
import json
import csv
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


all_vehicles_info = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

vehicle_count = len(all_vehicles_info)


# Locate the information about each top in the OnwardCalls

stop_info_list = []

for i in range(vehicle_count):
  
    
    # Check if the bus stop status is available then try to create a exception
    try: 
        OnwardCall = all_vehicles_info[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
        stop_name = OnwardCall[0]['StopPointName']
        stop_status = OnwardCall[0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        stop_name = 'N/A'
        stop_status = 'N/A'
    
    
    # Getting the coordinate of the buses
    
    location = all_vehicles_info[i]['MonitoredVehicleJourney']['VehicleLocation']
    latitude = location['Latitude']
    longitude = location['Longitude']
    
    # Create a list of dictionary to store all the information
    
    stop_info_list.append({'Latitude': latitude, 'Longitude': longitude, 'Stop Name': stop_name, 'Stop Status': stop_status})

# Convert the list of dictionary to a dataframe for a csv file conversion    

stop_info_df = pd.DataFrame(stop_info_list)

stop_info_df.to_csv(path_or_buf=sys.argv[3],index=False)