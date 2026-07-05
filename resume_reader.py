from pypdf import PdfReader

def load_resume(pdf_file):

    reader = PdfReader(pdf_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    return resume_text