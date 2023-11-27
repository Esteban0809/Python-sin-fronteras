# para esto necestaremos usar una libreria
import os

#este es del sistema operativo y nos permitira eliminar archivos y carpetas
path = 'E:\\Code\\Python\\Curso Python - Python Sin fronteras HTML CSS FLASK Y MYSQL\\Seccion 8\\'
if os.path.exists(path+'file.txt'):
    os.remove(path+'file.txt')
else:
    print("No se encontro el archivo")

# para eliminar carpetas
os.rmdir(path+'foldersin')