import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from django.shortcuts import render


def index(request):
    p = request.GET.get('QRid')
    url = 'https://items.sfc.keio.ac.jp/xml/gtin/' + p
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        xml_string = response.read()
        root = ET.fromstring(xml_string)
    d = {
        'root_tag': root.attrib
    }
    return render(request, 'index/index.html', d)

