from bs4 import BeautifulSoup as bs
import requests
from numpy import logical_not
import pandas as pd
acc = pd.Series([1, 2, 3, 4, 5])
acc += 10
print(acc)


url = 'https://www.dip.or.kr'
response = requests.get(url)
html = bs(response.text, 'html.parser')
logo = html.find('img')
print(logo)
