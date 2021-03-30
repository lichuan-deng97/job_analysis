import api.web_scraping.get_html_content as awsghc
import api.web_scraping.times as awst
from bs4 import BeautifulSoup

for page in range(1,6):
    url = f'https://www.shixiseng.com/interns?keyword=%E5%95%86%E4%B8%9A%E5%88%86%E6%9E%90&page={page}&city=%E5%85%A8%E5%9B%BD&type=intern'
    html = awsghc.get_url_content(url)
    soup = BeautifulSoup(html,"lxml")

    titles = soup.find_all(class_='title ellipsis font')
    for item in titles:
        detail_url = item.attrs['href']

        sub_html = awsghc.get_url_content(detail_url)
        sub_soup = BeautifulSoup(sub_html,"lxml")
        sub_titles = sub_soup.find(class_='new_job_name').attrs['title']
        sub_company_name = sub_soup.find(class_='com-name').string.strip() #strip()移除换行符，使title，company_name，location在同一行
        sub_location = sub_soup.find(class_='job_position').string
        sub_salary = sub_soup.find(class_='job_money cutom_font').string

        sub_salary = sub_salary.encode() # encode() 函数以指定的编码方式编码字符串
        sub_salary = sub_salary.replace(b'\xee\xba\xb1', b'1')
        sub_salary = sub_salary.replace(b'\xef\x9a\x98', b'2')
        sub_salary = sub_salary.replace(b'\xee\xa9\x83', b'0')
        sub_salary = sub_salary.replace(b'\xee\xa6\xa0', b'8')
        sub_salary = sub_salary.replace(b'\xef\x86\x9f', b'5')
        sub_salary = sub_salary.replace(b'\xee\xaf\x86', b'3')
        sub_salary = sub_salary.replace(b'\xee\xa5\xa5', b'4')
        sub_salary = sub_salary.decode() # decode() 函数指定的编码格式来解码字符串



        with open('data.商业分析实习.csv',"a") as f:
            f.write(sub_titles+','+sub_company_name+','+sub_location+','+sub_salary+','+detail_url+'\n')

        awst.time_sleep(2)
