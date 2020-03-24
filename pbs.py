import sys
from urllib import quote
import requests
from pyquery import PyQuery as pq

if len(sys.argv)<2:
    print("Usage: %s <keyword>" % sys.argv[0])
    exit(1)

url = 'https://tpb.party/search/'+quote(sys.argv[1])
strhtml = requests.get(url)
doc = pq(strhtml.text)
t=doc("#searchResult")
trs=t("tr")[1:-1]
for tr in trs:
    td=tr.getchildren()[1]
    name=td.getchildren()[0].text_content()
    a=td.getchildren()[1]
    link=a.attrib["href"]
    print name,link