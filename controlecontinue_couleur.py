def niveau_vers_points(niveau):
    niveau = niveau.strip().lower()

    if niveau in ["très bonne maîtrise", "tres bonne maitrise", "vert foncé", "vert fonce", "vert plus"]:
        return 50
    elif niveau in ["maîtrise satisfaisante", "maitrise satisfaisante", "vert clair", "vert claire"]:
        return 40
    elif niveau in ["maîtrise fragile", "maitrise fragile", "jaune"]:
        return 25
    elif niveau in ["maîtrise insuffisante", "maitrise insuffisante", "orange"]:
        return 10
    else:
        return None


competences = [
    "1. Comprendre, s’exprimer en utilisant la langue française à l’écrit et à l’oral",
    "2. Comprendre, s’exprimer en utilisant une langue étrangère ou régionale",
    "3. Comprendre, s’exprimer en utilisant les langages mathématiques, scientifiques et informatiques",
    "4. Comprendre, s’exprimer en utilisant les langages des arts et du corps",
    "5. Les méthodes et outils pour apprendre",
    "6. La formation de la personne et du citoyen",
    "7. Les systèmes naturels et les systèmes techniques",
    "8. Les représentations du monde et l’activité humaine"
]

print("=== Simulateur du Contrôle Continu (Socle Commun) ===")
print("Entrez votre niveau de maîtrise pour chaque compétence :")
print("Choix possibles : Très bonne maîtrise / Vert foncé / Maîtrise satisfaisante / Vert clair / Maîtrise fragile / Jaune / Maîtrise insuffisante / Orange\n")

total = 0
for competence in competences:
    while True:
        reponse = input(f"{competence} : ")
        points = niveau_vers_points(reponse)
        if points is not None:
            total += points
            break
        else:
            print("⚠️ Entrée invalide. Veuillez réessayer avec une des options valides.")

print(f"\n🎯 Score final du contrôle continu : {total} / 400")
