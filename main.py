import os
from scrapper import scrape_property_finder, scrape_bayut
from preprocessing import clean_data
from load_data import load_to_postgres


if __name__ == '__main__':
    print('Scrapping started..')
    scrape_bayut()
    scrape_property_finder()
    print('Scrapping done!')

    print('data preprocessing started..')
    cleaned_df = clean_data()
    print('Cleaning done!')

    print('loading to postgres..')
    load_to_postgres(cleaned_df, 'real_estate')
    print('Loading done!')

