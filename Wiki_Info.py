import requests, json
from lxml import etree

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

  #Make the request for the page requested by the user
  result_url = 'https://en.wikipedia.org/wiki/%s' % page_title

  result_req = requests.get(result_url)

  store = etree.fromstring(result_req.text)

  #Look for the college motto
  output = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')
  dict_items= {"Motto": output[0].text}
  
  return dict_items
#import requests
#import wikipedia
#from lxml import etree
#url = 'https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology'
#req = requests.get(url)
#store = etree.fromstring(req.text)
#output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')
#output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
#output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
#output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')
#print("Motto : "+output_motto[0].text)
#print("President : "+output_pres[0].text)
#print("Chancellor : "+output_chan[0].text)
#print("Location : "+output_loc[0].text)
