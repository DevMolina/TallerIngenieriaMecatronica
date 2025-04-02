from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_examen_burbujas(nombre_archivo="examen_burbujas.pdf", num_preguntas=10):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    
    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Hoja de Repuestas")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, "Nombre: ____________________________")
    c.drawString(50, height - 90, "Código: ____________________________")
    c.drawString(50, height - 110, "Fecha: ____________________________")
    
    # Dibujar opciones de respuesta una sola vez en la parte superior
    opciones = ["A", "B", "C", "D", "E"]
    x_pos = 95
    y_start = height - 130
    for opcion in opciones:
        c.drawString(x_pos, y_start, opcion)
        x_pos += 30  # Más espaciado entre opciones
    
    # Posiciones iniciales para las burbujas
    y_start -= 20  # Espaciado entre opciones y las preguntas
    spacing = 30  # Espaciado entre preguntas
    
    for i in range(1, num_preguntas + 1):
        c.drawString(50, y_start, f"{i}.")  # Número de pregunta
        x_pos = 100
        
        for _ in opciones:
            c.circle(x_pos, y_start, 8)  # Dibujar burbuja
            x_pos += 30 # Espaciado entre burbujas
        
        y_start -= spacing  # Espaciado entre preguntas
    
    c.save()
    print(f"Documento '{nombre_archivo}' generado con éxito.")

# Generar un examen con 20 preguntas
generar_examen_burbujas("examen.pdf", 20)