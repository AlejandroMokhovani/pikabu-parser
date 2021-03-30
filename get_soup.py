from bs4 import BeautifulSoup as bs

from list_of_comments import get_clear_comments


def get_users(story_id):
    # выбор нужного юзера
    user_need = 'silybum'
    soups = get_clear_comments(story_id)
    for soup in soups:

        soup = bs(soup, features='lxml')

        users_nicks = soup.find_all('span', 'user__nick')
        links_comments = soup.find_all('a', 'comment__tool hint')
        ratings = soup.find_all('div', 'comment__rating-count hint')

        for i in range(len(users_nicks)):
            if users_nicks[i].text == user_need:

                # users_nicks_list.append(users_nicks[i].text)
                # links_comments_list.append(links_comments[i]['href'])
                # ratings_text.append(ratings[i]['aria-label'])
                # ratings_summ.append(ratings[i].text)

                print(users_nicks[i].text)
                print(links_comments[i]['href'])
                print(ratings[i]['aria-label'])
                print(ratings[i].text)
