import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime


date = datetime.today().strftime('%Y-%m-%d')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

def scrape_property_finder():
    
    df = pd.DataFrame(columns=['Scraping_Date', 'Type', 'Description', 'Bedrooms', 'Bathrooms', 'Area', 'Down Payment', 'Price', 'Location'])

    for i in range(1, 40):
        url = f"https://www.propertyfinder.eg/en/search?c=1&fu=0&ob=mr&page={i}"
        reqs = requests.get(url, headers=headers)
        try:
            if reqs.status_code == 200:
                content = reqs.content
                soup = BeautifulSoup(content, 'html.parser')
                cards = soup.find_all('article', class_='property-card-module_property-card__wrapper__ZZTal')
                if cards:
                    for card in cards:
                        try:
                            p_type = card.find_all('p', class_='styles-module_content__property-type__QuVl4')[0].text
                            price = card.find_all('p', class_='styles-module_content__price__SgQ5p')[0].text
                            down_payment = card.find_all('div', class_='tag-module_tag__jFU3w')[0].text[13:] if card.find_all('div', class_='tag-module_tag__jFU3w') else 'Cash'
                            description = card.find_all('h2', class_='styles-module_content__title__eOEkd')[0].text
                            location = card.find_all('p', class_='styles-module_content__location__bNgNM')[0].text
                            sub_location = card.find_all('p', class_='styles-module_content__location__bNgNM')[0].text.split(',')[-2]
                            bedrooms = card.find_all('div', class_='styles-module_content__details__5sHyT')[0].find_all('p')[0].text.strip()
                            bathrooms = card.find_all('div', class_='styles-module_content__details__5sHyT')[0].find_all('p')[1].text.strip()
                            area = card.find_all('div', class_='styles-module_content__details__5sHyT')[0].find_all('p')[2].text
                            #mobile = card.find_all('a', {'data-testid':'property-card-contact-action-CALL'})[0]['href']
                            url = card.find_all('a', class_='property-card-module_property-card__link__L6AKb')[0].get('href')
                            df.loc[len(df.index)] = [date, p_type, description, bedrooms, bathrooms, area, down_payment, price, location]
                        except Exception as e:
                            print(e)
                else:
                    print('no cards found')
        except Exception as e:
            print(str(e))
    df.to_csv(f'data/property_finder_{date}.csv', index=False)

def scrape_bayut():

    df = pd.DataFrame(columns=['Scraping_Date', 'Type', 'Description', 'Bedrooms', 'Bathrooms', 'Area', 'Down Payment', 'Location', 'Price'])
    for i in range (1, 40):
        url = f'https://www.bayut.eg/en/egypt/properties-for-sale/page-{i}/'
        request = requests.get(url, headers=headers)
        try:
            if request.status_code == 200:
                content = request.content
                soup = BeautifulSoup(content, 'html.parser')
                cards = soup.find_all('li', class_='a37d52f0')
                for card in cards:
                    try:
                        price = card.find_all('span', class_='dc381b54')[0].text
                        description = card.find_all('h2', class_='f0f13906')[0].text
                        location = card.find_all('h3', class_='_4402bd70')[0].text
                        d_payment_tag = card.find_all('span', class_='_41163454')
                        d_payment = d_payment_tag[0].text if d_payment_tag else 'N/A'
                        listing_type = card.find_all('span', {'aria-label':'Type'})[0].text
                        bedrooms_tag = card.find_all('span', {'aria-label':'Beds'})
                        bedrooms = bedrooms_tag[0].text if bedrooms_tag else 'N/A'
                        bathrooms = card.find_all('span', {'aria-label':'Baths'})[0].text
                        area_tag = card.find_all('h4', class_='cfac7e1b _85ddb82f')
                        area = area_tag[0].text if area_tag else 'N/A'
                        df.loc[len(df.index)]= [date, listing_type, description, bedrooms, bathrooms, area, d_payment, location, price]
                    except Exception as e:
                        print(e)
            else:
                print('Status code error')
        except Exception as e:
            print(str(e))
    df.to_csv(f'data/bayut_{date}.csv', index=False)

if __name__ == '__main__':
    print('sorry cant run it, call it in main.py')