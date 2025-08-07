
# 🧠 Logique Métier

## 📌 Objectif de l’application

Permettre à un utilisateur de suivre et d’optimiser sa progression dans des decks de cartes à réviser, dans une logique proche de l’apprentissage par répétition espacée (SRS).

---

## 📍 Règles métier principales

### 1. Statut d'une carte

Chaque carte a un **statut** stocké dans `flashcards_user1_data.json` :

- `"à réviser"` : carte à revoir prochainement.
- `"acquise"` : carte maîtrisée, pas à revoir pour le moment.

> Ces statuts sont **la source principale** de vérité pour la progression.

---

### 2. Reviews

Les reviews sont un historique des réponses de l’utilisateur. Elles servent uniquement à **évaluer la carte**, et à **mettre à jour son statut**.

> On ne se base **plus** directement sur les `reviews` pour les calculs de progression dans les graphiques.

---

## 📊 Utilisation des statuts pour les visualisations

### ➤ Statistiques globales : `/status_progress.html`
- Basé uniquement sur les statuts `"acquise"` vs `"à réviser"`.
- Les données sont extraites du fichier `flashcards_user1_data.json`.

### ➤ Statistiques par deck : `/dashboard.html`
- Basé sur le taux de bonnes réponses (`"correct"`) dans les `reviews`.
- Sert à suivre la progression **historique** par deck.

---

## 🧩 Extension possible

- Intégrer un algorithme de SRS pour automatiser le changement de statut.
- Ajout de rappels par mail pour les cartes à revoir.
- Liaison avec une base PostgreSQL pour multi-utilisateur.
