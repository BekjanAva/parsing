import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

def get_html(url):
    r = requests.get(url)
    # print(r.text)
    return r.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table', class_='table').find_all('td')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'http://kenesh.kg' + a
        links.append(link)


    # for i in links:
    #     print(i)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('h3', class_='deputy-name').text.strip()
    except:
        name = ''
    try:
        number = soup.find('p3', class_='mb-10').text.strip()
    except:
        number = ''
    try:
        bio = soup.find('div', id='biography').text.strip()
    except:
        bio = ''


    data = {
        'name':name,
        'number':number,
        'bio':bio
    }
    print(data)
    return data


def write_csv(data):
    with open('deputat.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['name'],
            data['number'],
            data['bio']
        ))
        print(
            data['name'],
            data['number'],
            data['bio']
        )

def main():
    start = datetime.now()
    url = 'http://kenesh.kg/ky/deputy/list/35'
    html = get_html(url)

    all_links = get_all_links(html)
    for link in all_links:
        html = get_html(link)
        data = get_page_data(html)
        write_csv(data)
    end = datetime.now()
    result = end - start
    print(str(result))


if __name__ == '__main__':

    main()
