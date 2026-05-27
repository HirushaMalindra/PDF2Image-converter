import fitz
import os

def pdf_to_img(pdf_path, output_folder):
    """Convert each page of the PDF to an image and saves them."""
    os.makedirs(output_folder, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        output_path = f"{output_folder}/page_{page_number + 1}.png"
        pix.save(output_path)
        print(f"saved: {output_path}")

    pdf_document.close()

    
