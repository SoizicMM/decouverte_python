import random

vie_ennemi = 50
vie_joueur = 50
potions = 3

while True:
  # Jeu du joueur
  joueur = input("Veux tu Attaquer (1) ou une Potion (2) ?")

  if joueur == "1":  # Attaque
    attaque_joueur = random.randint(5, 10)
    vie_ennemi = vie_ennemi - attaque_joueur
    # exemple: print("Tu infliges xxxxx dégats")
    print(f"Tu infliges {attaque_joueur} points de dégats à l'ennemi ⚔️")
  elif joueur == "2"and potions > 0:  # Potion 
    points_potion = random.randint(10, 20)
    vie_joueur = vie_joueur + points_potion
    potions = potions - 1
    print(f"Tu récupères {points_potion} points de vie ❤️ (reste {potions})")
  else:
    print("Tu n'as plus de potion..")
    continue


  # Attaque de l'ennemi
  attaque_ennemi = random.randint(5, 15)
  vie_joueur = vie_joueur - attaque_ennemi
  print(f"L'ennemi t'inflige {attaque_ennemi} points de dégats ⚔️")


  # Récapitulatif du tour
  print(f"Il te reste {vie_joueur} points de vie.")
  print(f"Il reste {vie_ennemi} points de vie à l'ennemi.")
  print("-" * 50)


  # Fin de partie
  if vie_ennemi <= 0:
    print("Bravo, tu as gagné !!")
    break
  elif vie_joueur <= 0:
    print("Dommage, tu as perdu...")
    break
    