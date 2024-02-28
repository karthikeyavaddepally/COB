#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

api_key = '03731cc40e9a77b94e53f77c938030a1'
city = 'Warangal'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
print(url)
# Fetch the weather data
response = requests.get(url)
data = response.json()
# Create a pandas DataFrame with the weather data
weather_data = pd.DataFrame({
    'city': [city],
    'temperature': [data['main']['temp']],
    'humidity': [data['main']['humidity']],
    'pressure': [data['main']['pressure']],
    'wind_speed': [data['wind']['speed']],
    'wind_direction': [data['wind']['deg']],
    'cloudiness': [data['clouds']['all']],
    'weather_description': [data['weather'][0]['description']]
})
df = pd.DataFrame(weather_data)

# Convert DataFrame to CSV file
df.to_csv('weather.csv', index=False)  


# In[2]:


weather_updates = pd.read_csv('weather.csv')


# In[3]:


print(weather_updates)


# In[ ]:




