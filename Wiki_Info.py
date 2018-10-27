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

    if 'Established' in result:
        result['Established'] = result['Established'].strip().split()[0]
    return {key.strip():result[key].strip() for key in result}

    #Look for the college motto
    output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')

    dict_items={}

    if len(output_motto) >= 1:
        print('Motto: ' + output_motto[0].text)
        dict_items['Motto']=output_motto[0].text

    else:
        print('[!]No motto here')


    # Looking for College Chancellor name
    output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')

    if(len(output_chan)>= 1):
        print("Chancellor: "+output_chan[0].text)
        dict_items['Chancellor'] = output_chan[0].text

    else:
        print('[!]No Chancellor found')

    #Looking for college President
    output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
    if(len(output_pres)>=1):
        print("President: "+output_pres[0].text)
        dict_items['President']=output_pres[0].text
    else:
        print('[!]No President found')

    #Looking for College Location
    output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
    if(len(output_loc)>= 1):
        print("Location: "+output_loc[0].text)
        dict_items["Location"]=output_loc[0].text
    else:
        print('[!]No Location Found')

    #Look for the college motto
    output = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')

    return dict_items
