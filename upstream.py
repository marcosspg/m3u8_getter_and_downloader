import requests;
import re;
import utils;
import jsunpack;



def getEval(url):
    with requests.Session() as s:
        response = s.get(url);
        encontrado = re.findall('<script type[=]\'text\/javascript\'>eval.*',response.text)[0];
        return encontrado;


def unpack(eval):
    return jsunpack.unpack(eval);




def downloadFile(url, filename, autoUploadToMixdrop):
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
    utils.downloadFile(url, filename, autoUploadToMixdrop);