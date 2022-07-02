### Note must pip install pyinstaller in order to create executable ###
### Used 'pyinstaller --onefile example.py' to create the executable file ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

# run selenium headless
options = Options()
options.headless = True

#open the news webpage
driver = webdriver.Chrome(options=options)
driver.get("https://www.thesun.co.uk/sport/football/")

# find all the elements with this XPATH
containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')

# empty lists
titles = []
subtitles = []
links = []

# get the title, subtitle, and link for each news story
for container in containers:
    # since we are looping through containers we can use '.' instead of writing the entire div path
    title = container.find_element(By.XPATH, './a/h2').text
    subtitle = container.find_element(By.XPATH, './a/p').text
    link = container.find_element(By.XPATH, './a').get_attribute("href")
    # store the data in lists
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()