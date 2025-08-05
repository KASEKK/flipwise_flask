# 📊 FlipWise – Data & Visualisation

Ce dossier contient les éléments liés à la visualisation des données utilisateurs, à intégrer dans la page d'accueil de l'application FlipWise.

---

## 🎯 Objectif du graphique

Offrir à l'utilisateur une **vue synthétique de sa progression**, en affichant :
- Le **pourcentage global de réussite** sur tous ses decks de révision
- Une **distinction claire** entre les cartes acquises et celles encore à revoir

Cela permet à l’utilisateur de :
- visualiser ses efforts,
- identifier ce qu’il reste à travailler,
- être motivé à compléter ses decks.

---

## 📁 Contenu du dossier

| Fichier | Description |
|--------|-------------|
| `data_simulation.json` | Données simulées contenant 1 utilisateur, 5 decks, et 6 cartes par deck, avec des statuts (`acquise`, `à revoir`, `révisée`) |
| `graphique_progression.py` | Fonction Python générant un graphique circulaire (camembert) à partir des données simulées |
| `resultat_graphique.png` | Aperçu visuel du graphique généré, destiné à être intégré dans la page d'accueil |
| `README.md` | Présentation du livrable et instructions de collaboration |

---

## ⚙️ Instructions

### 💻 1. Tester le graphique
Ouvrir le fichier `graphique_progression.py` dans un environnement comme **Jupyter Notebook** ou **VS Code**.

Lancer le script pour générer un aperçu du graphique (`resultat_graphique.png`).

### 🔄 2. À implémenter côté front
- Le composant devra intégrer le graphique généré dynamiquement (via une API ou un service).
- La logique Python pourra être réécrite en TypeScript/JS si nécessaire, ou bien exposée par un backend si celui-ci existe.
- À discuter : est-ce que le front attend une image ou une structure de données à afficher dynamiquement via Chart.js, etc.

