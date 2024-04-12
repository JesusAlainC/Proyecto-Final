import fitz
import re

def extraer_texto(pdf_file):
    texto = ""
    documento = fitz.open(pdf_file)
    for pagina in documento:
        texto += pagina.get_text("text")
    return texto

def comparar_pdf(pdf_file1, pdf_file2):
    texto1 = extraer_texto(pdf_file1)
    texto2 = extraer_texto(pdf_file2)

    frases1 = set(texto1.split('\n\n')) 
    frases2 = set(texto2.split('\n\n'))

    palabras1 = set(re.findall(r'\b\w+\b', texto1))
    palabras2 = set(re.findall(r'\b\w+\b', texto2))

    frases_comunes = frases1.intersection(frases2)
    palabras_comunes = palabras1.intersection(palabras2)

    return frases_comunes, palabras_comunes

def crear_pdf_desde_texto(texto, output_pdf_file):
    pdf = fitz.open()
    pagina = pdf.new_page()
    y = 50
    for item in texto:
        pagina.insert_text((50, y), item)
        y += 15
    pdf.save(output_pdf_file)

pdf_file1 = "archivo1.pdf"
pdf_file2 = "archivo2.pdf"

frases_comunes, palabras_comunes = comparar_pdf(pdf_file1, pdf_file2)

output_pdf_file = "resultado.pdf"
crear_pdf_desde_texto(list(frases_comunes) + list(palabras_comunes), output_pdf_file)

print(f"Proceso completado. Archivo PDF creado: {output_pdf_file}")
