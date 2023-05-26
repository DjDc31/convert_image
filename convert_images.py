from PIL import Image

class Convert_images:

    def convert_image(input_path, output_path, output_format):
        # Ouvrir l'image d'entrée
        image = Image.open(input_path)

        # Convertir l'image dans le format spécifié
        image.save(output_path, format=output_format)

        print(f"L'image a été convertie en {output_format} et enregistrée à {output_path}")
