import requests
from lxml import etree
def find_college(name):
    print("Searching for the college")
    req = requests.get(r'https://en.wikipedia.org/w/index.php?search={}'.format(str(name)))
    if 'Search results' in req.text:
        print("No such page exists. Are you sure you have spelled right? Please select from the following results")
        soup = BeautifulSoup(req.text, 'lxml')
        all_ = ['https://en.wikipedia.org' + x.find('a').get('href') for x in soup.findAll('div', class_="mw-search-result-heading")]
        leng = list(range(len(all_)))
        list_of_search_results = [(y, x.text) for x,y in zip(soup.findAll('div', class_="mw-search-result-heading"), leng)]
        print(list_of_search_results)
        selected_entry = 99
        n = input("Please input the number. If none, then type N")
        if n.lower() == 'n':
            print("Please close the terminal")
        else:
            if int(n) in leng:
                selected_entry = n
            else:
                print("INVALID ENTRY, Please close the terminal")
        if selected_entry is not int('99'):
            req = requests.get(all_[int(selected_entry)])
    store = etree.fromstring(req.text)
    output_motto = store.xpath('//table[@class="infobox vcard"]/tbody/tr[th/text()="Motto"]/td/i')
    output_loc = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[15]/td/span[1]/a')
    output_pres = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td/a')
    output_chan = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[8]/td/a')
    print("Motto : "+output_motto[0].text)
    print("President : "+output_pres[0].text)
    print("Chancellor : "+output_chan[0].text)
    print("Location : "+output_loc[0].text)
