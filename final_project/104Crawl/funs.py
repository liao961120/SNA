import requests
from bs4 import BeautifulSoup

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