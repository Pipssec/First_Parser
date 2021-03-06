from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


data = []
browser = webdriver.Chrome(executable_path=r"C:\Users\Home\Downloads\chromedriver\chromedriver.exe")
url = 'https://bus.gov.ru/registry'
browser.get(url)
input_tab = (browser.find_element_by_tag_name('input'))
input_tab.send_keys('онкологический диспансер')
button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()
sleep(10)
for p in range(10):

    soup = BeautifulSoup(browser.page_source, "html.parser")

    orgs = soup.findAll('div', class_='result')

    for org in orgs:
        try:
            name = org.find('a', class_='result__title').text.strip()
        except:
            name = org.find('div', class_='result__common_title').text.strip()

        link = "https://bus.gov.ru/registry" + org.find('a', class_='result__button_registry').get('href')
        data.append([name, link])

    print(len(data))
    try:
        browser.find_element_by_class_name('pagination__next').click()
    except:
        break
    sleep(5)

header = ['name', 'link']
df = pd.DataFrame(data, columns=header)
df.to_csv('dispanser_data.csv', sep=';', encoding='utf8')
