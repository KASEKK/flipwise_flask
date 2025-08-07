
# 📚 FlipWise

FlipWise est une mini-application Flask pour visualiser la progression d'un utilisateur dans des decks de cartes à réviser, dans une logique proche des flashcards type Anki.

---

## 🔧 Fonctionnalités

- Visualisation de la progression **par deck** (via `/api/progress`)
- Visualisation de la progression **globale** (via `/api/status-progress`)
- Deux vues HTML avec graphiques interactifs Chart.js :
  - `/` → Vue par deck
  - `/status` → Vue globale (acquises vs à réviser)

---

## 🗂️ Structure du projet

```
FlipWise/
├── app.py                     # API Flask
├── static/
│   ├── deck_progress.json     # Données par deck
│   ├── card_status_progress.json  # Données globales (à partir des statuts des cartes)
│   └── flashcards_user1_data.json # Données utilisateur avec statut des cartes
├── templates/
│   ├── dashboard.html         # Vue par deck
│   └── status_progress.html   # Vue globale
├── doc/
│   ├── architecture_data.md   # Documentation data
│   └── logique_metier.md      # Documentation métier
└── README.md
```

---

## 🚀 Lancer le projet en local

1. Crée un environnement virtuel :
```bash
conda create -n flipwise-data python=3.10
conda activate flipwise-data
pip install flask
```

2. Lance l’app :
```bash
python app.py
```

3. Accède aux pages :
- Vue deck : [http://localhost:5000/](http://localhost:5000/)
- Vue globale : [http://localhost:5000/status](http://localhost:5000/status)

---

## 🧑‍💻 Pour les développeurs frontend

Tu peux intégrer les graphiques directement avec Chart.js. Il suffit de faire :

```js
fetch('/api/status-progress')
  .then(response => response.json())
  .then(data => {
    // utilise data.acquises_percent et data.à_revoir_percent
  });
```

Et de faire pareil avec `/api/progress` pour le détail par deck.

---

## 📌 À venir

- Authentification multi-utilisateur
- Export/Import de sessions
- Algorithme de SRS personnalisé
