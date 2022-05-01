#! python3
# Daily Text

# Open

import webbrowser, requests
from bs4 import BeautifulSoup

URL = 'https://wol.jw.org/en/wol/h/r1/lp-e/2022/5/1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="dailyText")
# print(results.prettify())

job_elements = results.find_all("div", id="dailyText")

for job_element in job_elements:
    text_date = job_element.find("h2", class_="p88")
    # text_scripture = job_element.find("p", class_="p3")
    # location_element = job_element.find("p", class_="p4")
    # print(text_date)
    # print(text_scripture)
    # print(location_element)
    print()