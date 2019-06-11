import requests
from bs4 import BeautifulSoup

def get_dept_urls(headers_, url='https://www.104.com.tw/jb/career/department/navigation?browser=1&degree=3&sid=5003000000'):
    response = requests.get(url, headers=headers_)
    response.encoding = 'utf-8'
    dom = BeautifulSoup(response.text, 'html.parser')
    # Get index to every dept.
    links = dom.find_all('a', class_='a2')
    # Get links to all dept.
    dept_links = []
    for link in links:
        dept = link.text
        href = 'https://www.104.com.tw' + link['href']
        dept_links.append((dept, href))
    return dept_links


def parse_dept(dept, url, headers_, out='dept_info.csv'):
    # Request
    resp = requests.get(url, headers=headers_)
    resp.encoding = 'utf-8'
    
    # Parse HTML
    dom = BeautifulSoup(resp.text, 'html.parser')
    
    # 直接升學
    wawa1 = dom.find('div', class_='wawa1').find('div', class_='cnt').text.strip('%')
    # 先工作後升學
    wawa2 = dom.find('div', class_='wawa2').find('div', class_='cnt').text.strip('%')
    # 不再進修
    wawa3 = dom.find('div', class_='wawa3').find('div', class_='cnt').text.strip('%')
    # 延修率與師生比
    lst = [li.text for li in dom.find_all('li', class_='cf')]
    #postpone = lst[1].strip('% ：延修率')
    prof_stud = lst[-2].strip('師生比： ').replace('：', '/')
    prof_stud = round(eval(prof_stud), 4)

    # Write to csv
    with open(out, 'a', encoding='utf-8') as f:
        out_str = ','.join([dept, wawa1, wawa2, wawa3, str(prof_stud)])
        f.write(out_str + '\n')