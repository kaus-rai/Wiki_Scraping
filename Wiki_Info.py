import requests, json
from lxml import etree
from bs4 import BeautifulSoup

def scraper(college):
    #Tested with University of Toronto, Chan Sui Ki, University of Santo Tomas, Far Eastern University,
    #University of Michigan and more...

    #Get the real page title through wikipedia eng api
    url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=%s' % college

    req = requests.get(url)

    #Fetch the json data
    output = json.loads(req.text)
    #take the first matching result
    page_title = output['query']['search'][0]['title']
    page_id = output['query']['search'][0]['pageid']
    print('Found page with title "%s" and id %s' % (page_title,page_id))

    #Make the request for the page requested by the user
    result_url = 'https://en.wikipedia.org/wiki?curid=%d' % page_id

    result_req = requests.get(result_url).text
    soup = BeautifulSoup(result_req,features='lxml')
    table = soup.find('table',class_='infobox vcard')
    result = {}
    for row in table.find_all('tr'):
        if row.find('th'):
            result[row.find('th').text] = row.find('td').text
    return {key.strip():result[key].strip() for key in result}
