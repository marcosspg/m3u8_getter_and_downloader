import requests;
import re;
import utils;
import jsunpack;



def getEval(url):
    with requests.Session() as s:
        response = s.get(url);
        return re.findall('eval.*',response.text)[0];


def unpack(eval):
    return jsunpack.unpack(eval);




def downloadFile(url, filename, autoUploadToMixdrop):
    eval = getEval(url);
    jsunpacked = unpack(eval);
    url = str(re.findall('file:".*"}],image', jsunpacked)[0]).replace('file:"', '').replace('"}],image','');
    utils.downloadFile(url, filename, autoUploadToMixdrop);
