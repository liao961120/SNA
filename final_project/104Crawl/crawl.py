import requests
from bs4 import BeautifulSoup
from time import sleep
from funs import *

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
url = 'https://www.104.com.tw/jb/career/department/navigation?browser=1&degree=3&sid=5003000000'


# Get index to every dept.
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text

dom = BeautifulSoup(html, 'html.parser')
links = dom.find_all('a', class_='a2')

# Get links to all dept.
dept_links = []
for link in links:
    dept = link.text
    href = 'https://www.104.com.tw' + link['href']
    dept_links.append((dept, href))


with open('dept_info.csv', 'w', encoding='utf-8') as f:
    f.write('dept,直接升學,先工作後升學,不再進修,師生比\n')
# Crawl and save data
count = 0
for dept, url in dept_links:
    print('Parsing', dept, '...', count)
    parse_dept(dept, url, headers)
    count += 1
    print('Sleep for 0.5sec')
    sleep(0.5)

"""
url = 'https://www.104.com.tw/jb/career/department/view?degree=3&sid=5003000000&mid=420107'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text
dom = BeautifulSoup(html, 'html.parser')

# 直接升學
wawa1 = dom.find('div', class_='wawa1').find('div', class_='cnt').text.strip('%')
# 先工作後升學
wawa2 = dom.find('div', class_='wawa2').find('div', class_='cnt').text.strip('%')
# 不再進修
wawa3 = dom.find('div', class_='wawa3').find('div', class_='cnt').text.strip('%')
# 延修率與師生比
lst = [li.text for li in dom.find_all('li', class_='cf')]
postpone = lst[1].strip('% ：延修率')
prof_stud = lst[2].strip('師生比： ').replace('：', '/')
prof_stud = round(eval(prof_stud), 4)

with open('out.csv', 'a') as f:
    out_str = ','.join(['dept', wawa1, wawa2, wawa3, postpone, str(prof_stud)])
    f.write(out_str)
"""
