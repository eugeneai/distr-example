import requests as rq
from lxml import etree

URL="http://localhost:6543/howdy.json"

URLXML="http://localhost:6543/howdy.xml"

def processxml(xml):
    root = etree.fromstring(xml)
    val = root.xpath("/hello/name/text()")[0]
    print(val)
    val = root[0].text
    print(val)



def main():
    r = rq.get(URL)
    # print(r.text)
    print(r.json()["name"])
    r = rq.get(URLXML)
    t = r.content
    processxml(t)

if __name__ == '__main__':
    main()
