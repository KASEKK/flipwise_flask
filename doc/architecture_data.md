
# 📐 Architecture Data

## 🧱 Structure des entités principales

L'application repose sur un modèle relationnel cohérent conçu pour anticiper des besoins futurs (statistiques, adaptabilité, filtrage, exportation). Voici les principales entités et leurs relations :

- `users` ⟶ 1:N ⟶ `decks`
- `decks` ⟶ 1:N ⟶ `cards`
- `users` ⟶ 1:N ⟶ `reviews`
- `cards` ⟶ 1:N ⟶ `reviews`

---

## 📊 Visualisation de la progression

Deux visualisations principales sont générées avec Chart.js via Flask :

### 1. `/api/progress` → `dashboard.html`

Affiche la progression par deck, en pourcentage de bonnes réponses (historique basé sur les `reviews` avec rating `"correct"`).

Utilisation :
```js
fetch('/api/progress')
```

---

### 2. `/api/status-progress` → `status_progress.html`

Affiche une vue d'ensemble de la progression globale, selon le **statut courant des cartes** (`"acquise"` ou `"à réviser"`), stocké dans le fichier `flashcards_user1_data.json`.

Le calcul se base uniquement sur les statuts des cartes **et non plus les reviews**. Cela permet d’avoir un état réel à un instant T.

Utilisation :
```js
fetch('/api/status-progress')
```

---

## 🔁 Données dynamiques

Toutes les données (deck progress, status global) sont générées depuis des notebooks Python et sauvegardées dans `/static` sous forme de fichiers `.json`.

