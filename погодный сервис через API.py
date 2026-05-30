import requests

city = input("Введите город: ")
response = requests.get(f"https://wttr.in/{city}?format=j1")
data = response.json()

temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
max_temp = data["weather"][0]["maxtempC"] 
min_temp = data["weather"][0]["mintempC"]  
humidity = data["current_condition"][0]["humidity"] 

print("Температура:", temp, "°C")
print("Погода:", weather)
print("Max температура: ", max_temp)
print("Min температура: ", min_temp)
print("Влажность: ", humidity)