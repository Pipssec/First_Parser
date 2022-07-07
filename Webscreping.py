import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


url = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020'
page = requests.get(url).text
soup = BeautifulSoup(page, features="html.parser")
headline = soup.find('h1').get_text()
p_tags = soup.find_all('p')
p_tags_text = [tag.get_text().strip() for tag in p_tags]
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
article_text = ' '.join(sentence_list)
summary = summarize(article_text, ratio=0.3)
print(f'Length of original article: {len(article_text)}')
print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
print(f'Article Summary:\n{summary}')
#Работает на интерпретаторе 3.8
