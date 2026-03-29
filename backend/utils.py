import PyPDF2
import re

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text, skills_list):
    found_skills = []
    for skill in skills_list:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)
    return found_skills

def calculate_score(found, required):
    return int((len(found) / len(required)) * 100)