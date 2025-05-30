from fpdf import FPDF
import unicodedata

# Fonction pour nettoyer les caractères non pris en charge


def nettoyer(texte):
    texte = texte.replace("📚", "").replace("📝", "").replace("–", "-")
    texte = texte.replace("’", "'").replace("“", '"').replace("”", '"')
    return unicodedata.normalize('NFKD', texte).encode('latin-1', 'ignore').decode('latin-1')


# Planning d'étude fusionné
planning_etude = [
    ("Jeu, 29 mai", "Maths + Physique-Chimie"),
    ("Ven, 30 mai", "Français (grammaire) + Technologie"),
    ("Sam, 31 mai", "Histoire (2e Guerre mondiale) + Physique-Chimie"),
    ("Dim, 1er juin", "📝Examen blanc de maths + Correction des erreurs"),
    ("Lun, 2 juin", "Français (écriture) + Révision d’histoire"),
    ("Mar, 3 juin", "Maths (fonctions) + Français (lecture)"),
    ("Mer, 4 juin", "Physique-Chimie + Technologie"),
    ("Jeu, 5 juin", "Histoire (Guerre froide) + EMC"),
    ("Ven, 6 juin", "Physique-Chimie + Maths (géométrie)"),
    ("Sam, 7 juin", "Français (dictée) + Technologie"),
    ("Dim, 8 juin", "📝Examen blanc de français + Correction des erreurs"),
    ("Lun, 9 juin", "Révision d’histoire + Révision de physique-chimie"),
    ("Mar, 10 juin", "Maths (statistiques et probas) + Français (oral)"),
    ("Mer, 11 juin", "Physique-Chimie + Technologie"),
    ("Jeu, 12 juin", "Histoire-Géographie + EMC + Cartes"),
    ("Ven, 13 juin", "📝Test de physique-chimie + Correction des erreurs"),
    ("Sam, 14 juin", "Révision de français + Révision de maths"),
    ("Dim, 15 juin", "📝Examen blanc général (tout) + Correction des erreurs"),
    ("Lun, 16 juin", "Fiches + résumés + Révision légère uniquement")
]

# Création du PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_title(nettoyer("Plan d’étude du Brevet : du 29 mai au 16 juin"))

# En-tête
pdf.set_font("Arial", style="B", size=16)
pdf.cell(0, 10, nettoyer(
    "📚 Plan d’étude du Brevet : du 29 mai au 16 juin"), ln=True, align="C")
pdf.ln(5)

# En-tête du tableau (2 colonnes)
pdf.set_font("Arial", style="B", size=12)
pdf.cell(50, 10, "Date", border=1)
pdf.cell(140, 10, "Activités prévues", border=1)
pdf.ln()

# Remplissage du tableau
pdf.set_font("Arial", size=11)
for jour, activites in planning_etude:
    pdf.cell(50, 10, nettoyer(jour), border=1)
    pdf.cell(140, 10, nettoyer(activites), border=1)
    pdf.ln()

# Sauvegarde
chemin_pdf = "Planning_Etude_Brevet_2Colonnes.pdf"
pdf.output(chemin_pdf)

print(f"PDF généré : {chemin_pdf}")
