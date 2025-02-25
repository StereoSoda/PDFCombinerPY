import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
from io import BytesIO
from PIL import Image
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Desactivar el límite de seguridad de Pillow
Image.MAX_IMAGE_PIXELS = None

def combine_pdfs_from_directory(directory_path, output_path, dpi=300, batch_size=6):
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith(".pdf")]
    pdf_files.sort()

    if not pdf_files:
        print("No se encontraron archivos PDF en el directorio.")
        return

    writer = PdfWriter()

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%I-%M-%S%p").lower()
    output_filename = f"output_{timestamp}.pdf"
    output_path = os.path.join(output_path, output_filename)

    total_pages = 0
    pdf_images = []
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory_path, pdf_file)
        images = convert_from_path(pdf_path, dpi=dpi, fmt="png", thread_count=4)
        pdf_images.extend(images)
        total_pages += len(images)
    
    processed_tasks = 0
    print_progress_bar(processed_tasks, total_pages, prefix='Procesando', suffix=f'{processed_tasks}/{total_pages} Páginas')
    
    for i in range(0, len(pdf_images), batch_size):
        batch = pdf_images[i:i + batch_size]
        _process_images(batch, writer, dpi)
        processed_tasks += len(batch)
        print_progress_bar(processed_tasks, total_pages, prefix='Procesando', suffix=f'{processed_tasks}/{total_pages} Páginas')

    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"\nSe combinó con éxito el PDF, por favor revisar en: {output_path}")

def _process_images(images, writer, dpi):
    for i in range(0, len(images), 2):
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        img1 = images[i]
        can.drawImage(ImageReader(img1), 0, 396, width=612, height=396, preserveAspectRatio=True)
        if i + 1 < len(images):
            img2 = images[i + 1]
            can.drawImage(ImageReader(img2), 0, 0, width=612, height=396, preserveAspectRatio=True)
        can.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        writer.add_page(new_pdf.pages[0])

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█', print_end="\r"):
    gradient = [Fore.RED, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.GREEN]
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = ''
    for i in range(filled_length):
        color = gradient[i * len(gradient) // length]
        bar += f'{color}{fill}{Style.RESET_ALL}'
    bar += '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {Fore.YELLOW}{percent}%{Style.RESET_ALL} {suffix}', end=print_end)
    if iteration == total:
        print()

directory_path = "./input"
output_path = "./output"
combine_pdfs_from_directory(directory_path, output_path, dpi=300, batch_size=6)