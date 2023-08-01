import json

from bs4 import BeautifulSoup
import requests


url = "https://amib.ir/weblog/wp-content/uploads/amib/iran-provinces-cities/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

tbody = soup.find("tbody")

with open("cities.json", "w", encoding="utf-8") as file:
    city_list = []
    for tr in tbody.find_all("tr"):
        cells = tr.find_all('td')
        city_list.append(
            {cells[0].text.strip(): cells[1].text.strip()}
        )

    json.dump(city_list, file, ensure_ascii=False)