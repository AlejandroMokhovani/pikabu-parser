import requests
import fake_useragent
import lxml
import json


def get_all_comments(story_id):
    URL = 'https://pikabu.ru/ajax/comments_actions.php'

    user = fake_useragent.UserAgent().random
    story_id = story_id

    headers = {
        'User-Agent': user,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://pikabu.ru',
    }

    data = {
        'action': 'get_story_comments',
        'story_id': story_id
    }

    responce = requests.post(URL, headers=headers, data=data)


    json_responce = json.loads(responce.text)
    all_comments = json_responce['data']['comments']
    return all_comments

def get_clear_comments(story_id):
    list_of_comments = []
    all_comments = get_all_comments(story_id)
    for i in range(len(all_comments)):
        list_of_comments.append(all_comments[i]['html'])

    print(len(list_of_comments), 'comments', '<--', story_id)
    # print(list_of_comments)
    return list_of_comments

# print(get_clear_comments(6757200))
