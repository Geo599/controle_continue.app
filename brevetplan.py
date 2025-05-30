from datetime import date, timedelta
from fpdf import FPDF

# Clean text of unsupported characters


def clean(text):
    return text.replace("📚", "").replace("📝", "").replace("–", "-")


# Define the study plan (emojis and en-dashes are okay here; they'll be cleaned before PDF)
study_plan = [
    ("Wed, May 29", "Maths", "Physique-Chimie"),
    ("Thu, May 30", "French (grammar)", "Technologie"),
    ("Fri, May 31", "History (WWII)", "Physique-Chimie"),
    ("Sat, Jun 1", "📝Maths mock exam", "Review corrections"),
    ("Sun, Jun 2", "French (writing)", "History recap"),
    ("Mon, Jun 3", "Maths (functions)", "French (reading)"),
    ("Tue, Jun 4", "Physique-Chimie", "Technologie"),
    ("Wed, Jun 5", "History (Cold War)", "EMC"),
    ("Thu, Jun 6", "Physique-Chimie", "Maths (geometry)"),
    ("Fri, Jun 7", "French (dictation)", "Technologie"),
    ("Sat, Jun 8", "📝French mock exam", "Review corrections"),
    ("Sun, Jun 9", "History recap", "Physique-Chimie recap"),
    ("Mon, Jun 10", "Maths (stats & prob.)", "French (oral practice)"),
    ("Tue, Jun 11", "Physique-Chimie", "Technologie"),
    ("Wed, Jun 12", "History-Geography", "EMC + Maps"),
    ("Thu, Jun 13", "📝Physique-Chimie test", "Review corrections"),
    ("Fri, Jun 14", "French recap", "Maths recap"),
    ("Sat, Jun 15", "📝General mock (all)", "Review corrections"),
    ("Sun, Jun 16", "Flashcards + Summary", "Light review only")
]

# Create PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_title(clean("Brevet Study Plan: May 29 – June 16"))

# Header
pdf.set_font("Arial", style="B", size=16)
pdf.cell(0, 10, clean("📚 Brevet Study Plan: May 29 – June 16"), ln=True, align="C")
pdf.ln(5)

# Table header
pdf.set_font("Arial", style="B", size=12)
pdf.cell(50, 10, "Date", border=1)
pdf.cell(70, 10, "Morning Session", border=1)
pdf.cell(70, 10, "Afternoon Session", border=1)
pdf.ln()

# Table content
pdf.set_font("Arial", size=11)
for day, morning, afternoon in study_plan:
    pdf.cell(50, 10, clean(day), border=1)
    pdf.cell(70, 10, clean(morning), border=1)
    pdf.cell(70, 10, clean(afternoon), border=1)
    pdf.ln()

# Save the PDF
pdf_path = "Brevet_Study_Plan.pdf"
pdf.output(pdf_path)

print(f"PDF saved as {pdf_path}")
