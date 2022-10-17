import requests;
import re;
import utils;
import jsunpack;
import jsbeautifier.unpackers.packer as packer;



def getEval(url):
    with requests.Session() as s:
        response = s.get(url);
        return re.findall('eval.*',response.text)[0];


def unpack(eval):
    return jsunpack.unpack(eval);




def downloadFile(url, filename):
    print(filename);
    jsunpacked = unpack(getEval(url));
    url = str(re.findall('file:".*"}],image', jsunpacked)[0]).replace('file:"', '').replace('"}],image','');
    if not url.__contains__("https://"):
        servers = str(re.findall("p1=.*", url)[0]);
        server = "";
        if servers.__contains__("p2"):
            server = servers.split("&")[0].split("=")[1];
        else: 
            server = servers.split("=")[1];
        url="https://"+server+".upstreamcdn.co"+url
    utils.downloadFile(url, filename);