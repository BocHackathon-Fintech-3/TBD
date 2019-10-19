# SCRIPT THAT SCRAPES ALL REGISTERED CHARITIES IN CYPRUS
# DATA FROM THE MINISTRY OF FINANCE WEBSITE
import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get("https://www.mof.gov.cy/mof/tax/taxdep.nsf/charity_gr/charity_gr?openform").content, "html.parser")

charities = soup.find_all('tr')[1:]
charities_list = []
for charity in charities:
    charities_list.append(charity.text.strip())