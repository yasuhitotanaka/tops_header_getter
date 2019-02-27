import sys
import requests
import bs4
import csv
import datetime
from config.setting import TOP_NUMBER

search_keyword = ""

if len(sys.argv) > 1:
    try:
        search_keyword = ' '.join(sys.argv[1:])
    except:
        print("Argumenets are not valid.")

print('検索ワード {}'.format(search_keyword))

if search_keyword:
    search_url = 'https://www.google.co.jp/search?hl=ja&num=' + str(TOP_NUMBER) + '&q=' + search_keyword
    print("Access to Google was succeed!")
    request_from_google = requests.get(search_url)
    print("Getting search results is succeed!")
    request_from_google.raise_for_status()
    parce_result = bs4.BeautifulSoup(request_from_google.text, 'html.parser')
    links = parce_result.select('div > h3.r > a')
    
    j = 0
    for i in range(len(links)):
        url = links[i].get('href').split('&sq=U&')[0].replace('/url?q=', '')
        title = parce_result.select('div > h3.r > a')[i].text
        if 'https://' in url or 'http://' in url:
            try:
                header = parce_result.select('div > span.st')[j].text
                print('{}位: {}, URL: {}, 見出し: {}'.format(i, title, url, header))
                j += 1
            except:
                continue
print("OK")