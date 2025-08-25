import os
import re
from PyPDF2 import PdfReader, PdfWriter

# Define folder and regex
base_dir = os.path.dirname(__file__)
papers_dir = os.path.join(base_dir, 'pdfs')
mark_pattern = re.compile(r'\b[23]\s*marks?\b', re.IGNORECASE)

# Create a writer for the final output
output_pdf = PdfWriter()

# Loop through all PDFs in the papers folder
for filename in os.listdir(papers_dir):
    if filename.lower().endswith('.pdf'):
        filepath = os.path.join(papers_dir, filename)
        reader = PdfReader(filepath)

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and mark_pattern.search(text):
                output_pdf.add_page(page)

# Save final PDF
output_path = os.path.join(base_dir, "2-3_mark_pages.pdf")
if len(output_pdf.pages) > 0:
    with open(output_path, 'wb') as f_out:
        output_pdf.write(f_out)
    print(f"✅ PDF created: {output_path}")
else:
    print("❌ No pages with 2 or 3 markers found.")
