#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup as soup

def main():
    response = requests.get('http://thecatapi.com/api/images/get.php?format=html')
    html = soup(str(response.text))
    cat_url = str(html.findAll('img')[0].get('src'))

    form_data = {'webaddress': cat_url, 'negative': 'N', 'maxwidth': '180'}
    response = requests.post('http://www.glassgiant.com/ascii/ascii.php', data=form_data)

    html = soup(response.text)
    
    try:
        text = str(html.findAll('font')[0])
    except:
        sys.exit("It never terminaaaaaaaaaaates!!!11")
        
    html = soup(text.replace('<br>', '').replace('</br>', ''))

    print html.findAll('font')[0].string

if __name__ == "__main__":
    main()

