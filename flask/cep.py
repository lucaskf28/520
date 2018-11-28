import requests

re = requests.get("https://viacep.com.br/ws/08270630/json/")
print(re.json())