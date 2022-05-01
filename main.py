#! python3

##############################
#
# DAILY TEXT
# 
##############################

# To Do
# 1 Proof of concept
# 2 Get working with WOL
# 3 Make Discord Bot

##############################
# START OF PROGRAM

import requests, datetime
from bs4 import BeautifulSoup

def main():
    
    # Get's current date
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day

    # Passes current date to make daily URL
    URL = (f'https://wol.jw.org/en/wol/h/r1/lp-e/{year}/{month}/{day})') # URL = (f'https://wol.jw.org/en/wol/h/r1/lp-e/2022/5/2)')
    
    # Passes URL to page
    page = requests.get(URL)

    # Grabs page content and passes to soup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Searches soup for the Daily Text
    results = soup.find(id='dailyText') # elements = results.find_all('div', id='dailyText')
    
    # Match days date with daily text
    days_results = results.find('div', attrs={'data-date': f'{year}-0{month}-0{day}T00:00:00.000Z'})
    
    days_date = days_results.header.h2.get_text()
    days_quote = days_results.p.em.get_text()
    days_scripture = days_results.p.a.em.get_text()
    days_paragraph = days_results.find('div', class_='bodyTxt').get_text().strip()

    # Display daily text
    print(
f'''{days_date}

{days_quote}{days_scripture}
        
{days_paragraph}
        
URL: {URL} 
    ''')
    # print(days_results)

main()