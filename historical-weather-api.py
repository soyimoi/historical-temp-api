from calendar import c
import datetime as dt
from datetime import timezone
import requests
from csv import writer


# Set up of the API call 
# If api_key throws an error, add the full file path where you key is stored 

b_url = "http://api.weatherapi.com/v1/history.json?key="
api_key = open('API-key.txt', 'r').read()
city = "Kiruna" 

# Date must be formatted as yyyy-mm-dd

h_date = '2023-01-01'

# The final call should look something like

url = b_url + api_key + '&q=' + city + '&dt=' + h_date

# My color mapping

dark_green = [-17, -16, -15, -14, -13, -12, -11, -10, -9]
light_green = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
beige = [6, 7, 8, 9, 10, 11]
light_brown = [12, 13, 14, 15, 16, 17]
dark_orange = [18, 19, 20, 21, 22, 23]




with open('Historical_Weather.csv', 'w', encoding='utf8', newline='') as f:

    header = ['Date', 'Max Temperature', 'Min Temperature', "Average Temperature", "Color"]
    w = writer(f)
    w.writerow(header)
    
    # Specify the dates you would like to retrieve data from formatted as yyyy-mm-dd

    my_dates = ['2023-01-22','2023-01-23', '2023-01-24']

    for date in my_dates:
        h_date = date
        curr_url = b_url + api_key + '&q=' + city + '&dt=' + h_date
        
        try:
            r = requests.get(curr_url).json()
            
            date_to_write = h_date
            
            # The temp info is in Celcius

            max_temp = int(r['forecast']["forecastday"][0]["day"]["maxtemp_c"])
            min_temp = int(r['forecast']["forecastday"][0]["day"]["mintemp_c"])
            avg_temp = int(r['forecast']["forecastday"][0]["day"]["avgtemp_c"])

            if avg_temp <= -18:
                color = 'White'
            elif avg_temp in dark_green:
                color = 'Dark Green'
            elif avg_temp in light_green:
                color = 'Light Green'
            elif avg_temp in beige:
                color = 'Beige'
            elif avg_temp in light_brown:
                color = 'Light Brown'
            elif avg_temp in dark_orange:
                color = 'Dark Orange'
            else:
                color = 'Dark Brown'

            to_write = [date_to_write, max_temp, min_temp, avg_temp, color]
            w.writerow(to_write)
            
            

        except Exception as e:
            print('Oops! Something broke.')
    
    
    





