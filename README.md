# PDFCombinerPY from dflopez
Toma PDF's y los combina

# Instalación en Windows

## Instalaciones requeridas

```pip install PyPDF2 reportlab pdf2image Pillow colorama```	

Descargar e instalar Poppler:
 
-Ve a https://github.com/oschwartz10612/poppler-windows/releases.  
-Descarga la última versión de poppler para Windows (por ejemplo, poppler-23.11.0.zip).  
-Extrae el archivo ZIP en una carpeta, por ejemplo: C:\poppler.  
-Agrega la carpeta bin de poppler a tu variable de entorno PATH:  
-Haz clic derecho en "Este equipo" o "Mi PC" y selecciona "Propiedades".  
-Haz clic en "Configuración avanzada del sistema".  
-En la pestaña "Opciones avanzadas", haz clic en "Variables de entorno".  
-En "Variables del sistema", busca la variable PATH y haz clic en "Editar".  
-Agrega la ruta a la carpeta bin de poppler, por ejemplo: C:\poppler\bin.  
-Haz clic en "Aceptar" para guardar los cambios.  

# Instalación en MacOs

## Instalaciones requeridas
### En el path del script, ejecutar los siguientes comandos:
```python3 -m venv venv``` (Creará el entorno virtual para Python).  
```source venv/bin/activate``` (Activará el entorno virtual).  
```pip install PyPDF2 reportlab pdf2image Pillow colorama``` (Instalará las librerías necesarias para la ejecución del script, también mencionadas en el archivo requirements).

```deactivate``` (Para cerrar el entorno virtual, cuando se termine de utilizar el script).

# Pasos para usar
### Debe crear en el mismo path del script las carpetas "input" y "output".  
-En input debe ir el/los PDF's a combinar.  
-En output se generará el PDF combinado.  
-```python combine_pdfs.py``` (En Windows para ejecutar el script).  
-```python3 combine_pdfs.py``` (En MacOs con el entorno virtual activado para ejecutar el script).

### Notas
-El DPI se puede variar para la calidad requerida, todo depende de los recursos de la máquina. 


![alt text](https://www.python.org/static/img/python-logo.png)