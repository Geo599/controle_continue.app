import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import numpy as np

# Color to Score Mapping
color_score_map = {
    "Très bonne maîtrise (dark green)": 50,
    "Maîtrise satisfaisante (light green)": 40,
    "Maîtrise fragile (yellow)": 25,
    "Maîtrise insuffisante (orange)": 10
}

color_refs = {
    "Très bonne maîtrise (dark green)": (0, 100, 0),
    "Maîtrise satisfaisante (light green)": (144, 238, 144),
    "Maîtrise fragile (yellow)": (255, 255, 0),
    "Maîtrise insuffisante (orange)": (255, 165, 0)
}

competences = [
    "Comprendre, s’exprimer en utilisant la langue française",
    "Comprendre, s’exprimer en utilisant une langue étrangère",
    "Comprendre, s’exprimer en utilisant les langages mathématiques et scientifiques",
    "Comprendre, s’exprimer en utilisant les langages des arts et du corps",
    "Méthodes et outils pour apprendre",
    "Formation de la personne et du citoyen",
    "Systèmes naturels et systèmes techniques",
    "Représentations du monde et l’activité humaine"
]

def count_colors(img, color_defs, tolerance=40):
    img_np = np.array(img)
    counts = {}
    for label, rgb_ref in color_defs.items():
        dist = np.sqrt(np.sum((img_np - rgb_ref) ** 2, axis=2))
        match_pixels = dist < tolerance
        counts[label] = int(np.sum(match_pixels))
    return counts

def process_pdf(pdf_file, label):
    images = convert_from_bytes(pdf_file.read(), dpi=300)
    img = images[0]  # Only first page
    counts = count_colors(img, color_refs, tolerance=40, )

    st.markdown(f"### 🎯 Résultats pour {label}")
    for k, v in counts.items():
        st.write(f"• {k} → {v} pixels")

    if sum(counts.values()) == 0:
        st.warning("Aucune couleur détectée.")
        return 0

    dominant = max(counts.items(), key=lambda x: x[1])[0]
    score = color_score_map[dominant]
    st.success(f"🎓 Niveau dominant détecté : **{dominant}** → {score} points")
    return score

def niveau_vers_points(niveau):
    niveau = niveau.strip().lower()
    correspondance = {
        "très bonne maîtrise": 50,
        "maîtrise satisfaisante": 40,
        "maîtrise fragile": 25,
        "maîtrise insuffisante": 10
    }
    return correspondance.get(niveau, 0)

# --- App ---
st.title("🎓 Calculateur du Contrôle Continu du Brevet")

st.markdown("### 📄 Option 1 : Analyse automatique à partir de PDF avec cercles colorés")

pdf1 = st.file_uploader("📘 PDF Semestre 1", type="pdf", key="sem1")
pdf2 = st.file_uploader("📗 PDF Semestre 2", type="pdf", key="sem2")

use_manual = False

if pdf1 and pdf2:
    st.success("Fichiers reçus. Analyse des cercles colorés en cours...")
    score1 = process_pdf(pdf1, "Semestre 1")
    score2 = process_pdf(pdf2, "Semestre 2")

    avg_score = (score1 + score2) / 2
    total_points = round(avg_score * len(competences))
    note_sur_20 = round((total_points / 400) * 20, 2)

    st.markdown("---")
    st.subheader("✅ Résultat final estimé (PDF)")
    st.success(f"**Total des points :** {total_points} / 400")
    st.success(f"**Note sur 20 :** {note_sur_20} / 20")

else:
    use_manual = True
    st.warning("PDFs manquants ou incomplets. Passage à la saisie manuelle.")

if use_manual:
    st.markdown("### ✍️ Option 2 : Saisie manuelle par compétence")

    total_manual = 0

    for comp in competences:
        col1, col2 = st.columns(2)
        with col1:
            sem1 = st.selectbox(
                f"{comp} (Semestre 1)",
                ["Très bonne maîtrise", "Maîtrise satisfaisante", "Maîtrise fragile", "Maîtrise insuffisante"],
                key=comp + "_s1"
            )
        with col2:
            sem2 = st.selectbox(
                f"{comp} (Semestre 2)",
                ["Très bonne maîtrise", "Maîtrise satisfaisante", "Maîtrise fragile", "Maîtrise insuffisante"],
                key=comp + "_s2"
            )
        avg = (niveau_vers_points(sem1) + niveau_vers_points(sem2)) / 2
        total_manual += avg

    note_manual = round((total_manual / 400) * 20, 2)

    st.markdown("---")
    st.subheader("✅ Résultat final (manuel)")
    st.success(f"**Total des points :** {round(total_manual)} / 400")
    st.success(f"**Note sur 20 :** {note_manual} / 20")
