from flask import Flask , jsonify
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello_world():
	url = "https://www.iqair.com/world-air-quality-ranking"
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	input_tag = soup.find_all('tr')
	resp = {}
	data_list = []
	for i in input_tag:
	    td_list = i.find_all('td')
	    if len(td_list) == 0:
	        continue
	    data_list.append({
	        'rank' : td_list[0].find_all('b')[0].getText(),
	        'flaglink' : td_list[1].find_all('img')[0].get('src'),
	        'name' : td_list[2].find_all('a')[0].getText(),
	        'value' : td_list[3].find_all('span')[0].getText(),
	        'href' : td_list[2].find_all('a')[0].get('href')
	    })
	     
	resp['data']=data_list
	return jsonify(resp)

if __name__ == '__main__':
	app.run()