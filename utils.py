import asyncio
import uploadToMixdrop
from subprocess import call
import os;

def getCurrentPath():
    return __file__.replace("utils.py", "").replace("\\", "/");

def downloadFile(url, originalFilename, autoUploadToMixdrop):
    path = getCurrentPath()+"descargas";
    if not os.path.isdir(path):
        os.mkdir(path);
    filename = path+"/"+originalFilename+".mp4";
    print("######## Descargando "+originalFilename+" ########");
    call([getCurrentPath()+'/lib/gstreamer/bin/gst-launch-1.0.exe', "souphttpsrc", "location="+url, "!" ,"hlsdemux", "!", "filesink", "location="+filename, "-e", "-q"]);
    print("######## Se ha descargado "+filename+" ########");
    if autoUploadToMixdrop:
        if os.path.getsize(filename) >0:
            print("######## Subiendo "+filename+" a mixdrop ########");
            uploadData = asyncio.run(uploadToMixdrop.upload(filename));
            if uploadData["success"]:
                print("El archivo "+filename+" se ha subido correctamente ("+str(uploadData["result"]["fileref"])+")");
            else:
                print("Fallo al subir el archivo "+filename+": "+str(uploadData["result"]));
        else:
            print("El archivo "+filename+" no contiene datos");
    