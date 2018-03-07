import requests
base_url = "https://github.com/timeline.json"
req = requests.get(base_url)

if(req.status_code == 200) :
    print(req.json)
else :
    print("Error occured: "+str(req.status_code))
    
