import concurrent.futures

from multiprocessing import Pool
from list_of_comments import get_clear_comments
from get_soup import get_users


# 70 seconds with for
# 68 seconds with Pool

# 6757200
# 6757150


def list_of_comments(start, end):
    list_of_com = []
    for i in range(start, end, -1):
        list_of_com.append(i)
    return list_of_com

storis_id = list_of_comments(6757200, 6757150)

def main():
    with Pool(16) as p:
        p.map(get_users, storis_id)




    # for id in storis_id:
    #     get_users(id, 'silybum')





if __name__ == '__main__':
    main()
