import requests
from bs4 import BeautifulSoup

#headers_ = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

#url = 'https://www.104.com.tw/jb/career/department/view?degree=3&sid=5003000000&mid=210501'
#dom = get_dom(url)

def parse_job_cond(dept, dom):
    work = dom.find_all('div', class_='yearContent')
    if len(work) != 1:
        raise Exception('div.yearContent len == ' + str(len(work)))
    div_cf = work[0].find_all('div', class_='cf')
    if not (div_cf[0].find('h3').text == '新鮮人第一份工作' \
        or div_cf[1].find('h3').text == '畢業2~5年' \
        or div_cf[2].find('h3').text == '畢業5~10年'):
        raise Exception('h3 not found in one of the div_cf in ' \
              + str(dom.find('meta', property='og:title')))
    work_progress = dict()
        # 畢業 1、2-5、5-10 年
    for i in 0, 1, 2:
        experience = div_cf[i].find('h3').text
        sub_dict = dict()
        # 做什麼工作、在哪些行業
        dl = div_cf[i].find_all('dl')
        for j in 0, 1:
            job, data = dl_parser(dl[j])
            sub_dict[job] = data
        work_progress[experience] = sub_dict
    return {dept: work_progress,}

def parse_study_status(dept, url, headers_, out='dept_info.csv'):
    dom = get_dom(url, headers_)
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

def dl_parser(dl):
    if isinstance(dl, list):
        raise Exception('dl is list.')
    title = dl.find('dt').text
    if dl.find('dd', class_='nodata') is None:
        job_prct = [tuple(dd.text.split(' %')) for dd in dl.find_all('dd')]
    else:
        job_prct = None
    return title, job_prct

def get_dom(url, headers_):
    # Request
    resp = requests.get(url, headers=headers_)
    resp.encoding = 'utf-8'
    # Parse HTML
    dom = BeautifulSoup(resp.text, 'html.parser')
    return dom

"""
work = dom.find_all('div', class_='yearContent')
if len(work) != 1:
    print('div.yearContent len ==', len(work))
else:
    div_cf = work[0].find_all('div', class_='cf')
    if not div_cf[0].find('h3').text == '新鮮人第一份工作' \
           or div_cf[1].find('h3').text == '畢業2~5年' \
           or div_cf[2].find('h3').text == '畢業5~10年':
        print('h3 not found in one of the div_cf in', 
        str(dom.find('meta', property='og:title')))
    else:
        work_progress = dict()
        # 畢業 1、2-5、5-10 年
    for i in 0, 1, 2:
        experience = div_cf[i].find('h3').text
        sub_dict = dict()
        # 做什麼工作、在哪些行業
        dl = div_cf[i].find_all('dl')
        for j in 0, 1:
            job, data = dl_parser(dl[j])
            sub_dict[job] = data
        work_progress[experience] = sub_dict
    dict_ = {'戲劇系': work_progress,}
"""