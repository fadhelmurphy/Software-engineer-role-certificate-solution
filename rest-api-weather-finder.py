"""
A REST API contains weather details of various cities.
Given a city name, get the current temperature of the city.
To access the weather information, perform an HTTP GET request to:
https://jsonmock.hackerrank.com/api/weather?name=
‹name>
where < name > is the city name to query. The name not case-sensitive.

For example, a GET request to:
https://jsonmock.hackerrank.com/api/weather?
name=Dallas
will return the weather information for Dallas.

The response to a request is a JSON with the following 5 fields:
• page: the current page of the results
• per_page: the maximum number of results returned per page
• total: the total number of results
• total_pages: the total number of pages with results
• data: Either an empty array or an array of weather records as JSON objects. Return the data from the first record in the array. Each record has multiple properties but below properties are only needed for this question:
• name: city name for which we have queried [STRING]
• weather: weather conditions of the city in the format
"‹temperature > degree" [STRING] and value temperature here is an integer
"""

import os
import requests

def getTemperature(city_name):
    base_url = "https://jsonmock.hackerrank.com/api/weather"
    params = {"name": city_name}

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if there is any weather data
        if data["data"]:
            first_record = data["data"][0]
            city = first_record.get("name", "N/A")
            temperature_str = first_record.get("weather", "N/A")
            temperature = int(temperature_str.split()[0]) if temperature_str else None
            
            return temperature
        else:
            return f"No weather data found for {city_name}."
    else:
        return f"Failed to retrieve weather data. Status code: {response.status_code}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    name = input()

    result = getTemperature(name)

    fptr.write(str(result) + '\n')

    fptr.close()
