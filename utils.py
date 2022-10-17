from genericpath import isdir
from subprocess import call
import os;

def getCurrentPath():
    return __file__.replace("utils.py", "").replace("\\", "/");

def downloadFile(url, originalFilename):
    path = getCurrentPath()+"descargas";
    if not os.path.isdir(path):
        os.mkdir(path);
    filename = path+"/"+originalFilename+".mp4";
    print("######## Descargando "+originalFilename+" ########");
    call([getCurrentPath()+'/lib/gstreamer/bin/gst-launch-1.0.exe', "souphttpsrc", "location="+url, "!" ,"hlsdemux", "!", "filesink", "location="+filename, "-e", "-q"]);
    print("######## Se ha descargado "+filename+" ########");