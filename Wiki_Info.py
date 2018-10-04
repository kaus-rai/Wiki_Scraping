import requests
from lxml import etree

url = 'https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology'

req = requests.get(url)

store = etree.fromstring(req.text)

output = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')

print(output[0].text)
