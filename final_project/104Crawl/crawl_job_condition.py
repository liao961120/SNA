import requests
import pickle
from bs4 import BeautifulSoup
from random import random
from pprint import pprint
from time import sleep
from funs import *
from parse_dept import *

headers_ = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

dept_urls = get_dept_urls(headers_)

# Main Loop: Loop over all deparatments
dept_dict = dict()
count = 1
for dept, url in dept_urls:
    print('Parsing', dept, '...', count)  # feedback
    temp_dict = parse_job_cond(dept, get_dom(url, headers_))
    key = list(temp_dict.keys())[0]
    dept_dict[key] = temp_dict[key]
    count += 1  # feedback
    print('Sleep for 0.5sec')
    sleep(0.5 + random())

with open('dept_job.pkl', 'wb') as f:
    pickle.dump(dept_dict, f)