import webbrowser, requests
from bs4 import BeautifulSoup

URL = 'http://127.0.0.1:5500/test.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="one")
for i in results:
    h1 = results.find("h1")
    h2 = results.find("h2")
    p = results.find("p")
print(f"H1: {h1.text}, H2: {h2.text}, P: {p.text}") #.get_text()

# job_elements = results

# for job_element in job_elements:
#     h1 = job_element.find("h1")
#     h2 = job_element.find("h2")
#     p = job_element.find("p")
#     print(h1)
#     print(h2)
#     print(p)
#     print()