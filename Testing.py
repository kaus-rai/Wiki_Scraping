import requests, json
from lxml import etree
def scraper(name):
    url = 'https://en.wikipedia.org/wiki/'+name
    req = requests.get(url)
    store = etree.fromstring(req.text)
    output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')
    output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
    output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
    output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')
    dict_items={'Motto':output_motto[0].text, 'President':output_pres[0].text, 'Chancellor':output_chan[0].text, 'Location':output_loc[0].text}

    return (dict_items)
scraper(MIT)