from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def dibujar_formato(c, x_offset, y_offset, num_preguntas=20, margen_derecho=20):
    """
    Dibuja el formato de respuestas en una posición específica de la página.
    """
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_offset + 30, y_offset - 30, "Hoja de Respuestas")
    c.drawString(x_offset + 30, y_offset - 50, "Examen Taller Ing. Mecatrónica")
    c.setFont("Helvetica", 12)
    c.drawString(x_offset + 30, y_offset - 70, "Nombre: ________________________")
    c.drawString(x_offset + 30, y_offset - 90, "Código: _________________________")
    c.drawString(x_offset + 30, y_offset - 110, "Fecha: __________________________")
    
    # Dibujar opciones de respuesta
    opciones = ["A", "B", "C", "D", "E"]
    x_pos = x_offset + 75
    y_start = y_offset - 130
    espacio_opciones = 25  # Reducir espacio entre opciones para ajustar márgenes
    
    for opcion in opciones:
        c.drawString(x_pos, y_start, opcion)
        x_pos += espacio_opciones
    
    # Posiciones iniciales para las burbujas
    y_start -= 20  # Espaciado entre opciones y las preguntas
    spacing = 25  # Espaciado entre preguntas
    
    for i in range(1, num_preguntas + 1):
        c.drawString(x_offset + 30, y_start, f"{i}.")  # Número de pregunta
        x_pos = x_offset + 75
        
        for _ in opciones:
            c.circle(x_pos, y_start, 6)  # Reducir tamaño de burbuja
            x_pos += espacio_opciones
        
        y_start -= spacing  # Espaciado entre preguntas

def generar_examen_burbujas(nombre_archivo="examen_burbujas.pdf", num_preguntas=20):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    margen_lateral = 40  # Ajuste para no salirse del margen derecho
    espacio_columna = width / 2 - margen_lateral
    
    # Dibujar dos formatos en la misma hoja (izquierda y derecha)
    dibujar_formato(c, x_offset=margen_lateral, y_offset=height - 20, num_preguntas=num_preguntas)
    dibujar_formato(c, x_offset=espacio_columna, y_offset=height - 20, num_preguntas=num_preguntas)
    
    c.save()
    print(f"Documento '{nombre_archivo}' generado con éxito.")

# Generar un examen con 20 preguntas en dos columnas
generar_examen_burbujas("examen.pdf", 20)
