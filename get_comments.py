import requests
import fake_useragent
import lxml
import time

from bs4 import BeautifulSoup as bs

select_user = []


user = fake_useragent.UserAgent().random

headers = {
    'user-agent': user
}

URL = 'https://pikabu.ru/story/a_vdrug_8064126'

get_page = requests.get(URL, headers=headers)

soup = bs(get_page.text, features='lxml')

main_container_comments = soup.find(
    'div',
    'comments__container_main comments__container'
    )

nick_names = main_container_comments.find_all('span', 'user__nick')

rating_comments = main_container_comments.find_all(
    'div',
    'comment__rating-count hint'
    )

links_comments = main_container_comments.find_all('a', 'comment__tool')




# # clear rating
# for rating in rating_comments:
#     print(rating['aria-label'])


# # clear nicknames
# for names in nick_names:
#     print(names.string)

# # clean link
# for link in links_comments:
#     print(link['href'])

# clear nick, rating and link
# for i in range(len(nick_names)):
#     print(
#         nick_names[i].string, '||',
#         rating_comments[i]['aria-label'], '||',
#         links_comments[i]['href']
#         )
# print(user)
# print(len(nick_names))

def find_this_nick(nick):
    for i in range(len(nick_names)):
        if nick_names[i].string == nick:
            select_user.append(
                nick_names[i].string + '||' +
                rating_comments[i]['aria-label'] + '||' +
                links_comments[i]['href']
                )

    return

find_this_nick('RN105')

for i in select_user:
    print(i)
