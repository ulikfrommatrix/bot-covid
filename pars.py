import requests

from bs4 import BeautifulSoup


URL = 'https://coronavirus-monitor.info/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://coronavirus-monitor.info'


def get_html(URL):
    r = requests.get(URL, headers=HEADERS)
    return r


def get_content(html):
    s = BeautifulSoup(html, 'html.parser')
    items = s.find('div', class_='confirmed').get_text(strip=True)
    its = []   #каждаяя статистика
    its.extend(items)
    # for item in items:
    #     its.extend(
    #         item.find('h2')
    #     )
    its.insert(8, ':\n')
    its.insert(19, '\nЗа сутки:     \n')
    its.insert(28, '\n\n\n')
    lst = ''.join(its)


    with open('stat.txt', 'w', newline='') as fil:
        fil.write(lst)



def get_cured(html):
    s = BeautifulSoup(html, 'html.parser')
    items = s.find('div', class_='cured').get_text(strip=True)
    its = []   #каждаяя статистика
    its.extend(items)
    # for item in items:
    #     its.extend(
    #         item.find('h2')
    #     )
    its.insert(8, ':\n')
    its.insert(19, '\nЗа сутки:     \n')
    its.insert(28, '\n\n\n')
    lst = ''.join(its)

    with open('stat.txt', 'a', newline='') as fil:
        fil.write(lst)

def get_curd(html):
    s = BeautifulSoup(html, 'html.parser')
    items = s.find('div', class_='deaths').get_text(strip=True)
    its = []  # каждаяя статистика
    its.extend(items)
    # for item in items:
    #     its.extend(
    #         item.find('h2')
        #     )
    its.insert(8, ':\n')
    its.insert(15, '\nЗа сутки:     \n')
    its.pop(7)
    its.insert(10, '\n')
    lst = ''.join(its)


    with open('stat.txt', 'a', newline='') as fil:
        fil.write(lst)
def parse():
    html = get_html(URL)

    get_content(html.text)
    get_cured(html.text)
    get_curd(html.text)




parse()


