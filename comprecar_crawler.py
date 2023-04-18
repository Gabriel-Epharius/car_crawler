import requests
from bs4 import BeautifulSoup


def get_car(car_name):
    return get_page(f'https://www.comprecar.com.br/buscar?busca={car_name}')

def get_page(url):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    
    page = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    return page

def get_list(page):
    list =[]
    for row in page.findAll('div', {'class': 'row vehicle-list'})[0].findAll('h2'):
        list.append(row.text)
    return list

def get_links(page):    
    links = []
    for car in page.findAll('div', {'class': 'row vehicle-list'})[0].findAll('a', href=True)[::3]:
        links.append(car.get('href'))
    return links


def get_maxpage(url):
    return int(get_page(url).findAll('a', {'class' : 'page-link'}, href=True)[-2].get('href').split('=')[-1])


def get_lastpage(url='https://www.comprecar.com.br/buscar?page=', page=0):
    last_page = get_maxpage(url + f'{page}')
    if  last_page> page:
        return get_lastpage(url, page=last_page)
    else: return page


