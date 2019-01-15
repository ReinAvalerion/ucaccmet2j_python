'''
### The big data
Load the JSON data and loop through it. We want you to calculate the monthly mm of rain for Seattle, as well as the total 
mm of rain over the whole year.

### Relatively rainy
Next, we want you to calculate the percentage of the yearly rain per month; i.e., if 20% of the rain in 2010 in Seattle fell in 
November, the corresponding value should read 0.2.

### Results
Save these results in a single JSON file called `result.json`. Save your data in a dictionary, where location name is the key, 
and the value is another dictionary, containing the corresponding state, weather station, precipitation per month, relative 
precipitation per month, total precipitation.
'''

# The big data

import json
with open('precipitation.json') as f: 
    my_list_dictionaries = json.load(f)

seattle = [0]*12

for measurement in my_list_dictionaries:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        month = int(measurement['date'].split('-')[1])
        # find rainfall for measurement (as integer)
        rainfall = measurement['value']
        # Add rainfall to right element of seattle list
        seattle[month-1] += rainfall

print(seattle)

year = sum(seattle)
print(year)

# Relatively rainy

monthly_relative_rainfall = []

for month_rainfall in seattle: 
    monthly_relative_rainfall.append(month_rainfall/year)
   

print(monthly_relative_rainfall)
