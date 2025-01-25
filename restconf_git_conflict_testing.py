def get_restconf_data(url, headers):
    response = requests.get(url, headers=headers, timeout=10) # Added timeout main
    return response.json()

def main():
    url = "https://apiexample.com/restconf/data" #changed url main
    headers = {"Content-Type": "application/json"}
    data = get_restconf_data(url, headers)
    print(f"RESTCONF Data: {data}") # Added formatted print main
