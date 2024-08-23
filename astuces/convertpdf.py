from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# import PyPDF2
# from googletrans import Translator

# with open("hacking.pdf","rb") as path :
#     pdfreader = PyPDF2.PdfReader(path)

#     for page_num in range(len(pdfreader.pages)) :
#         try :
#             page = pdfreader.pages[page_num]
#             text = page.extract_text()
#             t = Translator()
#             text = t.translate(text,dest='en').text
#             print(text)
#         except Exception as e:
#             pass

#     path.close()

def create_pdf_with_text(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, text)
    c.save()

create_pdf_with_text("text.pdf", "Ceci est un texte ajouté.")


# Ouvre le PDF existant
# with open("text.pdf", "rb") as f:
#     reader = PyPDF2.PdfReader(f)
#     writer = PyPDF2.PdfWriter()

#     # Ajoute toutes les pages du PDF existant au writer
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         writer.add_page(page)

#     # Écris le PDF modifié dans un nouveau fichier
#     with open("modified_text.pdf", "wb") as output_pdf:
#         writer.write(output_pdf)