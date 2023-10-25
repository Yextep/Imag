import os
from PIL import Image

def convertir_a_pdf(imagen_path, nuevo_path):
    imagen_obj = Image.open(imagen_path)
    imagen_obj.save(nuevo_path, "PDF", resolution=100.0, save_all=True)
    print(f"Imagen convertida a formato PDF: {nuevo_path}")

def cambiar_formato_imagenes(carpeta, nuevo_formato):
    try:
        # Verificar si la carpeta existe
        if not os.path.exists(carpeta):
            print("La carpeta especificada no existe.")
            return

        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(carpeta)

        # Definir las extensiones compatibles
        extensiones_compatibles = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")

        # Filtrar solo los archivos de imagen con las extensiones compatibles
        imagenes = [archivo for archivo in archivos if any(archivo.lower().endswith(ext) for ext in extensiones_compatibles)]

        if not imagenes:
            print("No se encontraron imágenes en la carpeta.")
            return

        # Crear un directorio para las imágenes convertidas
        carpeta_salida = os.path.join(carpeta, "imagenes_convertidas")
        os.makedirs(carpeta_salida, exist_ok=True)

        for imagen in imagenes:
            imagen_path = os.path.join(carpeta, imagen)

            imagen_obj = Image.open(imagen_path)

            if nuevo_formato.lower() == 'jpeg' and imagen_obj.mode == 'P':
                # Convertir la imagen de paleta (P) a modo RGB si el formato de salida es JPEG
                imagen_obj = imagen_obj.convert('RGB')
            
            nuevo_nombre = os.path.splitext(imagen)[0] + f".{nuevo_formato}"
            nuevo_path = os.path.join(carpeta_salida, nuevo_nombre)

            if nuevo_formato.lower() == 'pdf':
                convertir_a_pdf(imagen_path, nuevo_path)
            else:
                imagen_obj.save(nuevo_path, formato=nuevo_formato)

        print(f"Se han convertido {len(imagenes)} imágenes a formato {nuevo_formato} en '{carpeta_salida}'.")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def main():
    ubicacion = input("¿Dónde están ubicadas las imágenes? (Especifique la ruta o escriba 'actual' para la carpeta actual): ")

    if ubicacion.lower() == 'actual':
        carpeta = os.getcwd()
    else:
        carpeta = ubicacion

    print("Formatos de imagen disponibles: jpeg, png, bmp, gif, tiff, webp, pdf")
    nuevo_formato = input("Ingrese el formato al que desea convertir las imágenes: ")

    cambiar_formato_imagenes(carpeta, nuevo_formato)

if __name__ == "__main__":
    main()
