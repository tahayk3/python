from PIL import ImageFilter, ImageOps, ImageEnhance

# Función para aplicar el filtro blanco y negro
def aplicar_blanco_y_negro(imagen):
    return imagen.convert('L')

# Función para aplicar el filtro sepia
def aplicar_sepia(imagen):
    return ImageOps.colorize(imagen.convert("L"), "#704214", "#C0A080")

# Función para aplicar desenfoque gaussiano
def aplicar_borroso(imagen):
    return imagen.filter(ImageFilter.GaussianBlur(5))

# Función para ajustar el brillo
def ajustar_brillo(imagen, factor):
    enhancer = ImageEnhance.Brightness(imagen)
    return enhancer.enhance(factor)

# Función para ajustar el contraste
def ajustar_contraste(imagen, factor):
    enhancer = ImageEnhance.Contrast(imagen)
    return enhancer.enhance(factor)
