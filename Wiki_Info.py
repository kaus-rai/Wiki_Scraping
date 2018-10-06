import requests, json
from lxml import etree

#Tested with University of Toronto, Chan Sui Ki, University of Santo Tomas, Far Eastern University,
#University of Michigan and more...

#Take the input
college = input('[*]Enter college url: ')

#Get the real page title through wikipedia eng api
url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=%s' % college

req = requests.get(url)

#Fetch the json data
output = json.loads(req.text)
#print(output)

#take the first matching result
page_title = output['query']['search'][0]['title']
print(page_title)

#Make the request for the page requested by the user
result_url = 'https://en.wikipedia.org/wiki/%s' % page_title

result_req = requests.get(result_url)

store = etree.fromstring(result_req.text)

#Look for the college motto
output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')

if len(output_motto) >= 1:
  print('Motto: ' + output_motto[0].text)

else:
  print('[!]No motto here')

# Looking for College Chancellor name
output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')

if(len(output_chan)>= 1):
    print("Chancellor: "+output_chan[0].text)

else:
    print('[!]No Chancellor found')

#Looking for college President
output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
if(len(output_pres)>=1):
    print("President: "+output_pres[0].text)
else:
    print('[!]No President found')

#Looking for College Location
output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
if(len(output_loc)>= 1):
    print("Location: "+output_loc[0].text)
else:
    print('[!]No Location Found')
