# from multiprocessing import Process, Value, Array
#
# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#
#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])
#



# from multiprocessing import Manager, Pool
#
# input_list = ['A', 'B', 'C', 'D', 'E', 'F']
#
# manager = Manager()
# shared_list = manager.list()
#
# def do_stuff(element):
#     global shared_list
#     element_dict = {}
#     element_dict['name'] = element
#     shared_list.append(element_dict)
#     if len(shared_list) > 3:
#         print('list > 3')
#
# pool = Pool(processes=6)
# pool.map(do_stuff, input_list)
# pool.close()


import fake_useragent
import time
import requests
import concurrent.futures
import json


# def get_wiki_page_existence(wiki_page_url, timeout=10):
#     response = requests.get(url=wiki_page_url, timeout=timeout)
#
#     page_status = "unknown"
#     if response.status_code == 200:
#         page_status = "exists"
#     elif response.status_code == 404:
#         page_status = "does not exist"
#
#     return wiki_page_url + " - " + page_status

def get_wiki_page_existence(wiki_page_url):
    URL = 'https://pikabu.ru/ajax/comments_actions.php'

    user = fake_useragent.UserAgent().random
    story_id = wiki_page_url

    headers = {
        'User-Agent': user,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://pikabu.ru',
    }

    data = {
        'action': 'get_story_comments',
        'story_id': wiki_page_url
    }

    responce = requests.post(URL, headers=headers, data=data)


    json_responce = json.loads(responce.text)
    all_comments = json_responce['data']['comments']
    print(len(all_comments))
    return len(all_comments)


wiki_page_urls = [i for i in range(6757200, 6757150, -1)]

print("Running threaded:")
threaded_start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
print("Threaded time:", time.time() - threaded_start)


# import time
# import requests
# import concurrent.futures
#
#
# def get_wiki_page_existence(wiki_page_url, timeout=10):
#     response = requests.get(url=wiki_page_url, timeout=timeout)
#
#     page_status = "unknown"
#     if response.status_code == 200:
#         page_status = "exists"
#     elif response.status_code == 404:
#         page_status = "does not exist"
#
#     return wiki_page_url + " - " + page_status
#
# wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]
#
# print("Running without threads:")
# without_threads_start = time.time()
# for url in wiki_page_urls:
#     print(get_wiki_page_existence(wiki_page_url=url))
# print("Without threads time:", time.time() - without_threads_start)
