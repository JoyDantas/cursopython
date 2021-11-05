# WebScraping em Python

import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    voto = pergunta.select_one('.vote-count-post')

    print(data.text, titulo.text, voto.text, sep='\t')
