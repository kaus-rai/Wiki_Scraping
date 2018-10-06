import requests, json
from lxml import etree

#Tested with University of Toronto, Chan Sui Ki, University of Santo Tomas, Far Eastern University,
#University of Michigan and more...

#Take the input
college = input('Enter college url: ')

#Get the real page title through wikipedia eng api
url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=%s' % college

req = requests.get(url)

#Fetch the json data
output = json.loads(req.text)

#take the first matching result
page_title = output['query']['search'][0]['title']

#Make the request for the page requested by the user
result_url = 'https://en.wikipedia.org/wiki/%s' % page_title

result_req = requests.get(result_url)

store = etree.fromstring(result_req.text)

#Look for the college motto
output = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')

if len(output) >= 1:
  print(output[0].text)

else:
  print('[!]No motto here')