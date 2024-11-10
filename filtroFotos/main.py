from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import filters  # Importamos las funciones de filtros desde filters.py

# Inicializar variables globales
img = None
img_original = None
img_display = None

# Función para cargar imagen
def cargar_imagen():
    global img, img_original, img_display
    archivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if archivo:
        try:
            img = Image.open(archivo)
            img_original = img.copy()  # Guardamos la imagen original
            mostrar_imagen(img)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Función para mostrar imagen en el canvas
def mostrar_imagen(imagen):
    global img_display
    imagen_redimensionada = imagen.resize((500, 500), Image.Resampling.LANCZOS)  # Redimensionar la imagen para ajustarla al canvas
    img_display = ImageTk.PhotoImage(imagen_redimensionada)
    canvas.itemconfig(image_container, image=img_display)

# Filtros
def aplicar_filtro(filtro_func, factor=None):
    global img
    if img:
        if factor is not None:
            img = filtro_func(img, factor)
        else:
            img = filtro_func(img)
        mostrar_imagen(img)

def reiniciar_imagen():
    global img
    if img_original:
        img = img_original.copy()
        mostrar_imagen(img)

# Guardar imagen
def guardar_imagen():
    if img:
        archivo_guardar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if archivo_guardar:
            img.save(archivo_guardar)
    else:
        messagebox.showwarning("Advertencia", "Primero debes cargar una imagen.")

# Interfaz gráfica
ventana = Tk()
ventana.title("Aplicación de Fotografía con Filtros")

# Canvas para mostrar imagen
canvas = Canvas(ventana, width=500, height=500)
canvas.grid(row=0, column=0, columnspan=4)
image_container = canvas.create_image(350, 350, anchor=CENTER)

# Botones con estilos mejorados
btn_cargar = Button(ventana, text="Cargar Imagen", command=cargar_imagen, bg="#3498db", fg="white", padx=10, pady=5)
btn_cargar.grid(row=1, column=0, padx=10, pady=10)

btn_bn = Button(ventana, text="Blanco y Negro", command=lambda: aplicar_filtro(filters.aplicar_blanco_y_negro), bg="#2ecc71", fg="white", padx=10, pady=5)
btn_bn.grid(row=1, column=1, padx=10, pady=10)

btn_sepia = Button(ventana, text="Sepia", command=lambda: aplicar_filtro(filters.aplicar_sepia), bg="#e67e22", fg="white", padx=10, pady=5)
btn_sepia.grid(row=1, column=2, padx=10, pady=10)

btn_borroso = Button(ventana, text="Borroso", command=lambda: aplicar_filtro(filters.aplicar_borroso), bg="#9b59b6", fg="white", padx=10, pady=5)
btn_borroso.grid(row=1, column=3, padx=10, pady=10)

# Sliders para brillo y contraste
def actualizar_brillo(val):
    aplicar_filtro(filters.ajustar_brillo, float(val))

def actualizar_contraste(val):
    aplicar_filtro(filters.ajustar_contraste, float(val))

label_brillo = Label(ventana, text="Brillo")
label_brillo.grid(row=2, column=0, pady=5)

slider_brillo = Scale(ventana, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, command=actualizar_brillo)
slider_brillo.set(1.0)
slider_brillo.grid(row=2, column=1, pady=5, padx=10)

label_contraste = Label(ventana, text="Contraste")
label_contraste.grid(row=3, column=0, pady=5)

slider_contraste = Scale(ventana, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, command=actualizar_contraste)
slider_contraste.set(1.0)
slider_contraste.grid(row=3, column=1, pady=5, padx=10)

btn_reiniciar = Button(ventana, text="Reiniciar Imagen", command=reiniciar_imagen, bg="#34495e", fg="white", padx=10, pady=5)
btn_reiniciar.grid(row=4, column=0, pady=10)

btn_guardar = Button(ventana, text="Guardar Imagen", command=guardar_imagen, bg="#1abc9c", fg="white", padx=10, pady=5)
btn_guardar.grid(row=4, column=1, pady=10)

ventana.mainloop()
