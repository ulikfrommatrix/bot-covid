import requests

from bs4 import BeautifulSoup


URL = 'https://coronavirus-monitor.info/country/kyrgyzstan/'
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
    its.insert(15, '\nЗа сутки:     \n')
    its.insert(20, '\n\n\n')
    lst = ''.join(its)


    with open('stat_kg.txt', 'w', newline='') as fil:
        fil.write(lst)



def get_cured(html):
    s = BeautifulSoup(html, 'html.parser')
    items = s.find('div', class_='cured').get_text()
    its = []   #каждаяя статистика
    its.extend(items)
    # for item in items:
    #     its.extend(
    #         item.find('h2')
    #     )
    its.insert(8, ':\n')
    its.insert(15, '\nЗа сутки:     \n')
    its.insert(21, '\n\n\n')
    lst = ''.join(its)

    with open('stat_kg.txt', 'a', newline='') as fil:
        fil.write(lst)
def get_death(html):
    s = BeautifulSoup(html, 'html.parser')
    items = s.find('div', class_='deaths').get_text(strip=True)
    its = []  # каждаяя статистика
    its.extend(items)
    # for item in items:
    #     its.extend(
    #         item.find('h2')
        #     )
    its.insert(8, ':\n')
    its.insert(13, '\nЗа сутки:     \n')
    its.pop(7)
    its.insert(8, '6')
    its.insert(18, '\n\n\n')
    lst = ''.join(its)


    with open('stat_kg.txt', 'a', newline='') as fil:
        fil.write(lst)
def parser():
    html = get_html(URL)

    get_content(html.text)
    get_cured(html.text)
    get_death(html.text)




parser()
