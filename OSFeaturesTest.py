import requests
from bs4 import BeautifulSoup

KEY = "8sxgVXPjDNz4gW6FtBaATGVgqdWBqAEQ"


def get_capabilities():
    response = requests.get("https://api.os.uk/features/v1/wfs?service=wfs&request=getcapabilities&key=" + KEY)
    with open("capabilities.txt", "w") as output_doc:
        output_doc.write(str(response.content.decode()))


def get_feature():
    BASE = "https://api.os.uk/features/v1/wfs?service=wfs&version=2.0.0&request=GetFeature&count=100&key="
    response = requests.get(BASE)


ogc_filter = "<ogc:Filter>"
ogc_filter += "<ogc:PropertyIsEqualTo>"
ogc_filter += "<ogc:PropertyName>DescriptiveGroup</ogc:PropertyName>"
ogc_filter += "<ogc:Literal>Roadside</ogc:Literal>"
ogc_filter += "</ogc:PropertyIsEqualTo>"
ogc_filter += "</ogc:Filter>"
