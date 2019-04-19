import requests
from bs4 import BeautifulSoup
from random import uniform
import itertools as it


def get_html(url, useragent=None, proxy=None):
    req = requests.get(url, headers=useragent, proxies=proxy)
    return req.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', {'class':'paginator'})
    pages = div.find_all('a')[:-1]
    total_pages = pages[-1].text
    return int(total_pages)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    table_proxy_list = soup.find('table', {'id':'proxy_list'})

    ip_list = table_proxy_list.find_all('abbr').text
    port_list = table_proxy_list.find_all('span', {'class':'fport'}).text
    data = dict(zip(ip_list, port_list))

    return data

def write_data_to_file(data):
    with open('ip_list.txt', 'w') as f:
        for ip in data:
            f.write(ip + ':' + data[ip] + '\n')


def main():
    print('aada')
    country = 'TH'
    protocol = 'socks'
    sort_of = ['speed', 'ping']
    end_all = 'all'

    url = 'http://bit.ly/2P4qKP3'

    html = get_html(url)
    print(html)


    # ua ={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}
    # proxy = {'http': 'http://' + '91.185.222.11:80'}
    # # url = 'http://free-proxy.cz/en/proxylist/country/{}/{}/{}/{}/'.format(country, protocol, sort_of[0], end_all)
    # # url = 'http://free-proxy.cz/'
    # url = 'https://hidemyna.me/ru/proxy-list/?country=TH&type=4&anon=4#list'

    # print(requests.get('http://ipinfo.io/ip',proxies=proxy).text)
    # html = get_html(url, ua, proxy)
    # print(html)

main()
    # total_pages = get_total_pages(html)

    # data = get_page_data(html)

    # for number_page in range(1, total_pages):
    #     url_gen = url + str(number_page)
    #     html = get_html(url_gen)
    #     new_data = get_page_data(html)
    #     data.update(new_data)
    
    # write_data_to_file(data)
# if __name__ == 'main':
#     main()