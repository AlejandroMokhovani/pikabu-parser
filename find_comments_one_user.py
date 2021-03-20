import requests
import fake_useragent
import lxml
import json

from bs4 import BeautifulSoup as bs

users_nicks_list = []
links_comments_list = []
ratings_text = []
ratings_summ = []

def get_soup(story_id):
    URL = 'https://pikabu.ru/ajax/comments_actions.php'

    user = fake_useragent.UserAgent().random
    story_id = story_id

    headers = {
        'User-Agent': user,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://pikabu.ru'
    }

    data = {
        'action': 'get_story_comments',
        'story_id': story_id
    }

    responce = requests.post(URL, headers=headers, data=data)
    json_string = json.loads(responce.text)

    pre_soup = json_string['data']['comments']
    return pre_soup

def get_users(story_id, user_need):
    pre_soup = get_soup(story_id)
    for i in pre_soup:
        json_string_2 = i['html']
        soup = bs(json_string_2, features='lxml')

        users_nicks = soup.find_all('span', 'user__nick')
        links_comments = soup.find_all('a', 'comment__tool hint')
        ratings = soup.find_all('div', 'comment__rating-count hint')

        for i in range(len(users_nicks)):
            if users_nicks[i].text == user_need:

                users_nicks_list.append(users_nicks[i].text)
                links_comments_list.append(links_comments[i]['href'])
                ratings_text.append(ratings[i]['aria-label'])
                ratings_summ.append(ratings[i].text)


start = 6757200
end = 6757150

for i in range(start, end, -1):
    get_users(i, 'silybum')
    print(i)

print(users_nicks_list)
print(links_comments_list)
