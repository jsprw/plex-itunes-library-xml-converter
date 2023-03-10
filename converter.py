# https://github.com/jsprw/plex-itunes-library-xml-converter

import urllib.parse
import lxml.etree as ET
import sys

xmlfile = sys.argv[1]
resfile = sys.argv[2]
tree = ET.parse(xmlfile)
res = tree.findall('.//key[.="Location"]')

print("found " + str(len(res)) + " items.")

for el in res:
    location_el = el.getnext()
    location=urllib.parse.unquote(location_el.text, encoding="utf-8")
    try:
        location_el.text = urllib.parse.quote(location, safe='/:', encoding="cp1252")
    except  Exception as e:
        print()
        print('=== WARNING ===')
        print(e)
        print(location)
        print('===')
        

tree.write(resfile, pretty_print=True)