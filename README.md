# Convertidor de Imagenes (JPEG, PNG, GIF, PDF, TIFF, WEBP, BMP)

Este script permite al usuario elegir el formato al que desea convertir las imágenes. Utiliza la biblioteca PIL (Pillow) para el procesamiento de imágenes, solicita la carpeta que contiene las imágenes, pregunta el formato al que se quiere convertir y luego realiza la conversión. Las imágenes convertidas se guardarán en una nueva carpeta llamada "{nombre_carpeta}_convertido" que está ubicada en la ruta en donde el usuario ingresó la ubicación de las imágenes. El script maneja varios formatos de imagen, verifica la existencia de la carpeta y la presencia de imágenes antes de la conversión.

<img align="center" height="480" width="1000" alt="GIF" src="https://github.com/Yextep/Imag/assets/114537444/fe39ba28-1dbe-4977-bb2f-6b2cb05e74c4"/>


## Instalación

Clonamos el repositorio
```bash
git clone https://github.com/Yextep/Imag
```
Accedemos a la carpeta
```bash
cd Imag
```
Instalamos requerimientos
```bash
pip install -r requeriments.txt
```
Ejecutamos el Script
```bash
python3 imag.py
```
