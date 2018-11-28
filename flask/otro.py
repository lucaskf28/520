import requests, json

#re = requests.get("https://viacep.com.br/ws/08270630/json/")
#print(re.json())

headers = {"content-type" : "application/json"}
data = {"nome":"lucas bonitao"}

re = requests.post(
    "http://127.0.0.1:5000",
    #"http://httpbin.org/post",
    data=data
)
#print(re.json())