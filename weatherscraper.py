import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YNYNoxNKhO0'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id='seven-day-forecast')

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descriptions = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
long_descriptions = [d["title"] for d in seven_day.select(".tombstone-container img")]


pd.set_option('display.max_columns', None)  # display all columns (panda)

weather = pd.DataFrame({
    'period': periods,
    'short': short_descriptions,
    'temp': temps,
    'long': long_descriptions
})

print(weather)
