from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue#:~:text=This%20\
       list%20comprises%20the%20largest%20companies%20currently%20in%20the%20United'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


table = soup.find_all('table')[1]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]

df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data ]
    
    length = len(df)
    df.loc[length] = individual_row_data

print(df)    

df.to_csv(r'C:\Users\Modern\OneDrive\Desktop\DataScience\Week2Assignment\Top10LargestPrivateCompanies.csv', index= False)
