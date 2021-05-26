import random
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    response = requests.get('https://www.filmweb.pl/ranking/film')
    bs = BeautifulSoup(response.text, 'html.parser')
    data_dict = {'Title': [], 'Rating': [], 'Votes': []}
    all_data = pd.DataFrame(data = data_dict)

    title_data = bs.find_all("h2", {"class": "rankingType__title"})
    for indx, i in enumerate(title_data):
        all_data.at[indx,'Title'] = i.find('a').contents[0]

    rate_value = bs.find_all("span", {"class": "rankingType__rate--value"})
    for indx, i in enumerate(rate_value):
        all_data.at[indx,'Rating'] = str(i.contents[0]).replace(',', '.')

    rate_count = bs.find_all("span", {"class": "rankingType__rate--count"})
    for indx, i in enumerate(rate_count):
        all_data.at[indx,'Votes'] = str(i.find('span').contents[0].replace(' ', ''))

    
    indx = random.randrange(0, len(all_data))
    data_to_print = str(all_data.iloc[indx,:])
    data_to_print = data_to_print[:data_to_print.rfind('\n')]

    print("Recommended movie for today is: \n" + data_to_print)

    return True

if __name__ == '__main__':
    main()