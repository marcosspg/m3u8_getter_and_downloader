
import jsbeautifier.unpackers.packer as packer
import upstream
from _thread import start_new_thread
from tkinter import filedialog

filetypes = [('Archivos CSV', '*.csv')];

while True:
    print("""
1. Introducir url y nombre de archivo
2. Seleccionar csv (Delimitador por defecto ";" )
99. Salir
    """);
    opcion = input(": ");
    if opcion.strip() == "1":
        url = input("URL: ");
        filename = input("Nombre: ");
        print("""
Proveedor:
  1. upstream
        """);
        proveedor = input(": ");
        if proveedor.strip() == "1":
            start_new_thread(upstream.downloadFile, (url, filename,))
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
                        start_new_thread(upstream.downloadFile, (url, nombre,))
                inp.close();
            f.close();
    elif opcion == "99":
        exit();