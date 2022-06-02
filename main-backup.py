#! python3

# dailytext
# Author: Ashley Ball
# Repo: https://github.com/mrashleyball/dailytext
# Hosted: https://replit.com/@mrashleyball/dailytext

import requests, datetime, pytz
import discord
import os
from bs4 import BeautifulSoup

def dailytext():
  # Get AEST timezone
  AEST = pytz.timezone('Australia/Brisbane')
  
  # Get's current date, ensure AEST is used
  current_date = datetime.datetime.now(AEST)
  year = current_date.year
  month = current_date.month
  day = current_date.day
  
  # Passes current date to make daily URL
  URL = (f'https://wol.jw.org/en/wol/h/r1/lp-e/{year}/{month}/{day}')
  
  # Passes URL to page
  page = requests.get(URL)
  
  # Grabs page content and passes to soup
  soup = BeautifulSoup(page.content, 'html.parser')
  
  # Searches soup for the Daily Text
  results = soup.find(id='dailyText')
  
  # Add extra '0' to either month or day if needed
  if month < 10:
      month = '0'+str(month)
  if day < 10:
      day = '0'+str(day)
  
  # Match the days date with daily text
  days_results = results.find('div', attrs={'data-date': f'{year}-{month}-{day}T00:00:00.000Z'})
  
  # Extract text for the Date, Quote, Scripture and Paragraph from WOL based on HTML syntax
  days_date = days_results.header.h2.get_text()
  days_quote = days_results.find('p', class_='themeScrp').get_text()
  days_paragraph = days_results.find('div', class_='bodyTxt').get_text().strip()
  
  # Stores disclaimer message in variable
  disclaimer = 'Copyright © 2022 Watch Tower Bible and Tract Society of Pennsylvania.'
  
  # Display all elements that make the daily text including new lines, the link and disclaimer message
  days_text = days_date, days_quote, days_paragraph, URL, disclaimer

  return str(days_text).replace('\\xa',' ').replace('\\u', '')

client = discord.Client()
my_secret = os.environ['token']

@client.event
async def on_ready():
  print('We\'ve logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!dailytext'):
    the_days_text = dailytext()
    await message.channel.send(the_days_text)

client.run(os.environ['token'])