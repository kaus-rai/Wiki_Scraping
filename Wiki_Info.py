import requests
import wikipedia
from lxml import etree
url = 'https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology'
req = requests.get(url)
store = etree.fromstring(req.text)
output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')
output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')
print("Motto : "+output_motto[0].text)
print("President : "+output_pres[0].text)
print("Chancellor : "+output_chan[0].text)
print("Location : "+output_loc[0].text)

