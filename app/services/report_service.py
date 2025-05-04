from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
import openpyxl
from io import BytesIO

async def generate_grades_pdf(classroom_id: int):
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    
    data = [["Estudiante", "Materia", "Calificación"]]
    # ... obtener datos de la base de datos
    
    table = Table(data)
    pdf.build([table])
    
    buffer.seek(0)
    return buffer

async def generate_grades_excel(classroom_id: int):
    wb = openpyxl.Workbook()
    ws = wb.active
    
    # ... poblar datos
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer