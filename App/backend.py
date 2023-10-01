import requests
import os

# Parameters. They should be stored separately
api_key = os.environ.get('API_KEY')
base_api_url = os.environ.get('BASE_API_URL')
#base_api_url = "https://open-atms.airlab.aero/api/v1/"
#api_url = "https://open-atms.airlab.aero/api/v1/airac/airports"  # Replace with your API URL

# Define headers with the API key
headers = {
    "api-key": f"{api_key}"
}

## TODO, probably if there are many backend APIs, this function can be generalised
## TODO, can check frequency of data fetch. If data is not expected to change often, might make more sense to query 
## and cache locally with an option to force refresh

## Query backend server for SID information
def query_server_sid(airport_code):
    try:
        # Send a GET request to the API endpoint
        api_url = base_api_url + "airac/sids/airport/" + airport_code
        print("Querying api_url: " + api_url)
        response = requests.get(api_url, headers=headers, auth=None)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Display the response data
            print("Response Data:")
            print(data)
            #print("Title:", data.get("title"))
            #print("Body:", data.get("body"))
        else:
            print("Request failed with status code:", response.status_code)
    
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

## Calculate the SID based on the airport code
## Currently only supports WSSS
def calculate_stars(airport_code):
    if airport_code == "WSSS":
        response = query_server_sid(airport_code)        
        
        # Return results
        output = {
            "airport": "TEST",
            "topWaypoints": {
                "name": "TEST1",
                "count": "TEST2",
            }
        }        
    else:
        output = {
            "error": "Airport code invalid or not supported yet",
        }

    return output

## Calculate the SID based on the airport code
## Currently only supports WSSS
def calculate_sid(airport_code):
    if airport_code == "WSSS":
        response = query_server_sid(airport_code)
        
        # Return results
        output = {
            "airport": "TEST",
            "topWaypoints": {
                "name": "TEST1",
                "count": "TEST2",
            }
        }        
    else:
        output = {
            "error": "Airport code invalid or not supported yet",
        }          

    return output

# Testing mode if running locally
#query_server_sid("WSSS")