from urllib.request import Request, urlopen, HTTPError
from lxml import etree
import json
from json import JSONDecodeError
import requests
import lxml.html


def extract_word(url):

    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    response = urlopen(req)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)

    list_temp = []
    for li in tree.xpath('//ul/li'):
        if li.xpath('./a/@href'):
            word = li.xpath('./a/text()')
        else:
            word = li.xpath('./text()')
        if word:
            list_temp.append(word[0])

    return list_temp

list_url = [
    "https://martouf.ch/2009/06/liste-de-qualites/",
    "https://martouf.ch/2012/04/liste-de-mots-positifs/",
]

list_1 = get_word(list_url[0])[7:-23]
list_2 = get_word(list_url[1])[3:-23]
list_concat = list_1 + list_2

with open('mots_gentils.json', 'w') as outfile:
    json.dump(sorted(list_concat), outfile)
