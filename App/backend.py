import requests
import os

# Parameters which are defined in kubernetes cluster
api_key = os.environ.get('API_KEY')
base_api_url = os.environ.get('BASE_API_URL')

# Define headers with the API key
headers = {
    "api-key": f"{api_key}"
}

## TODO, probably if there are many backend APIs, this function can be generalised
## TODO, can check frequency of data fetch. If data is not expected to change often, might make more sense to query 
## and cache locally with an option to force refresh

## Query backend server for STARS information
def query_backend(api_url):
    try:
        # Send a GET request to the API endpoint
        print("Querying URL from backend: " + api_url)
        response = requests.get(api_url, headers=headers, auth=None)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Response from " + api_url + " is 200")
            # Parse the JSON response
            data = response.json()
            #print(json.dumps(data,indent=4))
            
            return data
        else:
            print("Request failed with status code:", response.status_code)
    
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        
    return None

## Calculate the SID based on the airport code
## Currently only supports WSSS
def get_top_stars(airport_code, count=2):
    
    # Query for the response with the provided airport_code
    #TODO this can be enhanced to query from local data source first, or to validate this with list of
    #of ICAO to see if this is a valid code
    api_url = base_api_url + "airac/stars/airport/" + airport_code
    stars_response = query_backend(api_url) 
    
    if stars_response is None or len(stars_response) == 0:
        output = {
            "error": "Airport code invalid or no results returned from airlab"
        }     
    else:
        # We have results, so we can find the top 2 waypoints by sorting
        stars_waypoints_sorted = sorted(stars_response, key=lambda x: len(x['waypoints']), reverse=True)
        
        output = {"airport":airport_code}
        
        # We use sorted list to iterate so we will never go out of bound
        topWaypoints = []
        for item in stars_waypoints_sorted:
            waypoint = {}
            waypoint['name'] = item['name']
            waypoint['count'] = len(item['waypoints'])
            topWaypoints.append(waypoint)
            
            # Once hit the count, can terminate
            if len(topWaypoints) >= count:
                break
            
        output['topWaypoints'] = topWaypoints    
      
    return output

## Select the top N SID based on the airport code. Default top 2 is returned
def get_top_sids(airport_code, count=2):
    # Query for the response with the provided airport_code
    #TODO this can be enhanced to query from local data source first, or to validate this with list of
    #of ICAO to see if this is a valid code
    api_url = base_api_url + "airac/sids/airport/" + airport_code
    sid_response = query_backend(api_url)
    
    if sid_response is None or len(sid_response) == 0:
        output = {
            "error": "Airport code invalid or no results returned from airlab",
        }     
    else:
        # We have results, so we can find the top 2 waypoints by sorting
        sid_waypoints_sorted = sorted(sid_response, key=lambda x: len(x['waypoints']), reverse=True)
        
        output = {"airport":airport_code}
        
        # We use sorted list to iterate so we will never go out of bound
        topWaypoints = []
        for item in sid_waypoints_sorted:
            waypoint = {}
            waypoint['name'] = item['name']
            waypoint['count'] = len(item['waypoints'])
            topWaypoints.append(waypoint)
            
            # Once hit the count, can terminate
            if len(topWaypoints) >= count:
                break
            
        output['topWaypoints'] = topWaypoints    
      
    return output

# Testing mode if running locally or debugging
#print(get_top_sids("WSSS",2))
#print(get_top_stars("WSSS",2))