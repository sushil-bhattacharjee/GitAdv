import requests

def get_restconf_data(url, headers):
    try:                                                         # Added error handling BRANCH
        response = requests.get(url, headers=headers, timeout=10) # Added timeout main
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RESTCONF data: {e}")
        return None

def main():
    url = "https://api.example.com/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback/0" #revised the url BRANCH
    headers = {"Content-Type": "application/yang-data+json", "Authorization": "Basic token"} # Added authorization header BRANCH
    data = get_restconf_data(url, headers)
    if data:
        print(f"RESTCONF Data: {data}") # Added formatted print main
    else:
        print("Failed to fetch RESTCONF data.")

if __name__ == "__main__":
    main()
