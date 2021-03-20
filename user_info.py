import requests
import fake_useragent
import lxml

from bs4 import BeautifulSoup as bs


user = fake_useragent.UserAgent().random

headers = {
    'user-agent': user
}

URL = 'https://pikabu.ru/@Yukto'

get_page = requests.get(URL, headers=headers)

soup = bs(get_page.text, features='lxml')

main_cont = soup.find_all('div', 'profile__section')

count_comments = main_cont[1].find_all('span')

result = count_comments[5].b.text

print(result)
