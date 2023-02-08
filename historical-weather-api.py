from datetime import datetime
import requests
from csv import writer
import pandas as pd


# Set up of the API call 
# If the api_key variable throws an error, add the full file path where you key is stored 

b_url = "http://api.weatherapi.com/v1/history.json?key="
api_key = open('/Users/soyimoi/Downloads/Python Projects/Historical Weather/API-key.txt', 'r').read()
city = "Kiruna" 

# Date must be formatted as yyyy-mm-dd

h_date = '2023-01-01'

# The final call should look something like

url = b_url + api_key + '&q=' + city + '&dt=' + h_date



with open('Historical_Weather.csv', 'w', encoding='utf8', newline='') as f:

    header = ['Date', 'Max Temperature', 'Min Temperature', "Average Temperature", "Color"]
    w = writer(f)
    w.writerow(header)
    
    # Specify the dates you would like to retrieve data from - format yyyy-mm-dd) 
    # First we select our desired range
    
    my_dates = pd.date_range(start="2023-01-23",end="2023-02-02")
    
    
    # Then we twick the format so our dates are str and not datetime objects
    
    my_final_dates = []

    for dtobj in my_dates:
        dtobj = dtobj.strftime('%Y-%m-%d')
        my_final_dates.append(dtobj)
        

    # Now we can loop through the dates and get the information we need 

    for date in my_final_dates:
        h_date = date
        curr_url = b_url + api_key + '&q=' + city + '&dt=' + h_date
        
        try:
            r = requests.get(curr_url).json()
            
            date_to_write = h_date
            
            # The temp info is in Celcius

            max_temp = int(r['forecast']["forecastday"][0]["day"]["maxtemp_c"])
            min_temp = int(r['forecast']["forecastday"][0]["day"]["mintemp_c"])
            avg_temp = int(r['forecast']["forecastday"][0]["day"]["avgtemp_c"])

            if min_temp <= -18:
                color = 'White'
            elif min_temp in range(-17, -8):
                color = 'Dark Green'
            elif min_temp in range(-8, 6):
                color = 'Light Green'
            elif min_temp in range(6, 12):
                color = 'Beige'
            elif min_temp in range(12, 18):
                color = 'Light Brown'
            elif min_temp in range(18, 24):
                color = 'Dark Orange'
            else:
                color = 'Dark Brown'

            to_write = [date_to_write, max_temp, min_temp, avg_temp, color]
            w.writerow(to_write)
            
            

        except Exception as e:
            print('Oops! Something broke.')
    
    
    





