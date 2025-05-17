
import upstream
import vtube
from _thread import start_new_thread
from tkinter import filedialog

filetypes = [('Archivos CSV', '*.csv')];
autoUploadToMixdrop = False;




while True:
    if autoUploadToMixdrop:
        autoUploadToMixdropTXT = "activado";
    else:
        autoUploadToMixdropTXT = "desactivado"
    print("""
1. Descargar por URL"""+
# 2. Seleccionar csv (Delimitador por defecto ";" )"""+
# 3. Subir automáticamente a mixdrop ("""+autoUploadToMixdropTXT+""")
"""99. Salir
    """);
    opcion = input(": ");
    if opcion.strip() == "1":
        url = input("URL: ");
        filename = input("Nombre: ");
        print("""
Origen del vídeo:
  1. upstream
  2. vtube
        """);
        proveedor = input(": ");
        if proveedor.strip() == "1":
            start_new_thread(upstream.downloadFile, (url, filename,autoUploadToMixdrop))
        if proveedor.strip() == "2":
            start_new_thread(vtube.downloadFile, (url.replace(".html", "").replace("embed-", ""), filename,autoUploadToMixdrop))
    elif opcion == "2":
        files = filedialog.askopenfiles(filetypes=filetypes, defaultextension=filetypes, title="Abrir csv para descargar");
        for f in files:
            ruta = f.name;
            with open(ruta, encoding="utf-8") as inp:
                for line in inp.readlines():
                    url = line.split(";")[0].strip();
                    proveedor = line.split(";")[1].strip();
                    nombre = line.split(";")[2].strip();
                    if proveedor == "upstream":
                        start_new_thread(upstream.downloadFile, (url, nombre,autoUploadToMixdrop))
                    if proveedor == "vtube":
                        start_new_thread(vtube.downloadFile, (url, nombre,autoUploadToMixdrop))
                inp.close();
            f.close();
    elif opcion == "3":
        autoUploadToMixdrop = not autoUploadToMixdrop;
    elif opcion == "99":
        exit();