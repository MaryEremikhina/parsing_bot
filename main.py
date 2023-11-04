import requests
from bs4 import BeautifulSoup
import json

# СОХРАНЕНИЕ ВСЕХ HTML САЙТОВ В КОНКРЕТНЫЕ ФАЙЛЫ

"""urls = {'url_mpo': 'https://predprof.olimpiada.ru/news',
        'url_shvb': 'https://olymp.bmstu.ru/ru/news',
        'url_vp': 'https://olymp.hse.ru/mmo/news',
        #'url_nto': 'https://ntcontest.ru/about/news/',
        'url_vsosh_tech': 'https://vos.olimpiada.ru/news',
        'url_enfuture': 'https://enfuture.ru/news/',
        'url_science_life': 'https://bmstu.ru/news',
        'url_kurchatov': 'https://olimpiadakurchatov.ru',
        #'url_step_medicine': 'https://kbsu.ru/events/16-04-2022-otkrytaja-olimpiada-shag-v-medicinu/',
        #'url_mgk': 'http://mgk.olimpiada.ru/#rec539507227'}
        }

for key in urls.keys():
    req = requests.get(urls[key])
    src = req.text
    with open(f'date/index_{key[4:]}.html', 'w') as file:
        file.write(src)"""

# ПАРСИНГ НОВОСТЕЙ ПРЕДПРОФА

"""with open('date/index_mpo.html') as f:
    src = f.read()

soup = BeautifulSoup(src, 'lxml')
news_getter = soup.find(class_='news').find_all(class_='news_item')
news = {}
for new in news_getter[:10]:
    new_name = new.find('span', class_='date red')
    news_about = new.find_all(class_='name with_arrow2')
    if len(news_about) == 1:
        new_about = news_about[0]
        new_href = new.find(class_='name with_arrow2').get('href')
        news[new_name.text] = [new_about.text, 'https://predprof.olimpiada.ru' + new_href]
    else:
        news_abouts = []
        for new_about in news_about:
            new_href = new_about.get('href')
            news_abouts.append([new_about.text, 'https://predprof.olimpiada.ru' + new_href])
        news[new_name.text] = news_abouts

#print(news)

    with open('news/mpo_news.json', 'w') as file:
        json.dump(news, file, indent=4, ensure_ascii=False)"""

# ПАРСИНГ НОВОСТЕЙ ШВБ

"""with open('date/index_shvb.html') as f:
    src = f.read()

soup = BeautifulSoup(src, 'lxml')
news_getter = soup.find(class_='block-system block-olymp-content').find(class_='views-rows').find_all(class_='mb30 views-row')
news = {}
for new in news_getter:
    new_about = new.find(class_='views-field views-field-title fz16').text
    new_href = 'https://olymp.bmstu.ru' + str(new.find(class_='views-field views-field-title fz16').find('span', class_='field-content').find('a').get('href'))
    new_name = new.find(class_='views-field views-field-body').find(class_='field-content').text
    new_time = new.find(class_='views-field views-field-field-date fz12 grey tar').find(class_='field-content').text
    if new_name == ' ':
        news[new_about] = [new_href, new_time]
    else:
        news[new_name] = [new_about, new_href, new_time]
print(news)

with open('news/shvb_news.json', 'w') as file:
    json.dump(news, file, indent=4, ensure_ascii=False)"""

