Ce document décrit les règles fonctionnelles à appliquer dans le projet, 
que ce soit via le mock json-server ou directement en Angular. 
Il remplace la logique backend par des comportements à simuler côté front.

-------------------------------------------------------------------

🔐 Création d’un utilisateur (simulé)
Quand l’utilisateur remplit un formulaire d’inscription :

Créer un objet user dans /users

S’assurer qu’il a un id, un username et un email unique

Pas besoin de vrai mot de passe → champ simulé ok

📦 Création d’un deck
Quand l’utilisateur crée un deck :

POST /decks avec name, description, et userId

Le front doit filtrer les decks par userId pour ne pas afficher ceux des autres

🃏 Ajout d’une carte
POST /cards avec deckId, question, answer, status = 'à revoir' par défaut

Chaque carte créée est directement liée à un deck

🎮 Quiz (très important à détailler)
Le front charge les cartes du deck : GET /cards?deckId=1

À chaque carte :

Quand l’utilisateur clique sur “Correct” ou “Incorrect” :

POST /reviews avec rating = correct|incorrect, userId, cardId

PATCH /cards/:id pour mettre à jour status = 'acquise' ou 'à revoir'

À la fin :

Le front doit calculer lui-même le score (GET /reviews?deckId=1&userId=1)

Puis proposer :

Rejouer toutes les cartes (GET /cards?deckId=1)

Ou seulement les ratées (GET /cards?deckId=1&status=à revoir)