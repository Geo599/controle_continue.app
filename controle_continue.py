import streamlit as st

# Mapping of niveaux de maîtrise to points


def niveau_vers_points(niveau):
    niveau = niveau.strip().lower()
    correspondance = {
        "très bonne maîtrise": 50,
        "vert foncé": 50,
        "maîtrise satisfaisante": 40,
        "vert clair": 40,
        "maîtrise fragile": 25,
        "jaune": 25,
        "maîtrise insuffisante": 10,
        "orange": 10,
    }
    return correspondance.get(niveau, 0)


# Liste des compétences
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

st.title("🎓 Calculateur du Contrôle Continu du Brevet")

st.markdown(
    "**Choisissez le niveau de maîtrise pour chaque compétence (Semestre 1 et 2)**")

total_points = 0
max_points = len(competences) * 100

for comp in competences:
    col1, col2 = st.columns(2)

    with col1:
        sem1 = st.selectbox(
            f"{comp} (Semestre 1)",
            ["Très bonne maîtrise", "Maîtrise satisfaisante",
                "Maîtrise fragile", "Maîtrise insuffisante"],
            key=comp + "_s1"
        )
    with col2:
        sem2 = st.selectbox(
            f"{comp} (Semestre 2)",
            ["Très bonne maîtrise", "Maîtrise satisfaisante",
                "Maîtrise fragile", "Maîtrise insuffisante"],
            key=comp + "_s2"
        )

    avg_score = (niveau_vers_points(sem1) + niveau_vers_points(sem2)) / 2
    total_points += avg_score

# Résultat final
st.markdown("---")
st.subheader("🧮 Résultat final")

score_sur_400 = round(total_points)
note_sur_20 = round((score_sur_400 / 400) * 20, 2)

st.write(f"**Total des points:** {score_sur_400} / 400")
st.write(f"**Note sur 20:** {note_sur_20} / 20")
