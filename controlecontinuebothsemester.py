def niveau_vers_points(niveau):
    niveau = niveau.strip().lower()
    if niveau in ["très bonne maîtrise", "tres bonne maitrise", "vert foncé", "vert fonce", "vert plus", "50"]:
        return 50
    elif niveau in ["maîtrise satisfaisante", "maitrise satisfaisante", "vert clair", "40"]:
        return 40
    elif niveau in ["maîtrise fragile", "maitrise fragile", "jaune", "25"]:
        return 25
    elif niveau in ["maîtrise insuffisante", "maitrise insuffisante", "orange", "10"]:
        return 10
    else:
        return 0


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

total = 0

print("🌟 Simulation du contrôle continu (sur 400 points)\n")
for comp in competences:
    print(f"\n{comp}")
    sem1 = input("   ➤ Niveau pour le 1er semestre : ")
    sem2 = input("   ➤ Niveau pour le 2e semestre : ")
    score1 = niveau_vers_points(sem1)
    score2 = niveau_vers_points(sem2)
    moyenne = (score1 + score2) / 2
    total += moyenne

print(f"\n🎯 Score total de contrôle continu : {int(total)} / 400")
