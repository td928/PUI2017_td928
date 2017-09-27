#Homework 2 


##Overview

This homework include three coding assignments. The first two involves using the MTA API to access bus information. The third
one requires manipulating a dataset within the CUSP data facility with Pandas DataFrame and creating plots with the data.


##Assignment 1

the first assignment is about retreiving the interested information in a JSON file and substract that information and print 
the information in the output.

Python provides very nice support to parse through JSON file by essentially treating it as a series of nested lists and 
dictionary. Then with useful function such as `dict.keys()` to list all the available keys in dictionary. It is very 
easy to quickly navigate through the JSON to fetch the longitude and latitude of each bus. 


##Assignment 2

Similar to the first assignment, assignment 2 also requires to parse through the JSON file. Only this time the interested
information is stored in the file under `OnwardCalls`. 

Unlike the first assignment, _OnwardCalls_ sometimes has missing information. Therefore, to account for the missing information
an exception catching mechanism is placed within the program.

'''python
try: 
    OnwardCall = all_vehicles_info[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
    stop_name = OnwardCall[0]['StopPointName']
    stop_status = OnwardCall[0]['Extensions']['Distances']['PresentableDistance']
except KeyError:
    stop_name = 'N/A'
    stop_status = 'N/A'
'''

Also since this assignment requires the output to be put into a csv file. So the information retreived was first stored
in a list of dictionary which later converted to a Panda Dataframe. Then with 

`stop_info_df.to_csv(path_or_buf=sys.argv[3],index=False)`

the dataframe is outputed as a csv file.


##Assignment 3

The assignment 3 requires the using dataframe function. Here I chose the data from projected population for New York. 

##Collaborator

This assignment is completed by Te Du alone. Some codes have referenced to the lab sessions made by Professor Bianco.
Her code can be found in her repository at [this address](https://github.com/fedhere/PUI2017_fb55) 

