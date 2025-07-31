📐 Architecture Data

🧱 Structure des entités principales
L'application repose sur un modèle relationnel cohérent conçu pour anticiper des besoins futurs (statistiques, adaptabilité, filtrage, exportation). Voici les principales entités et leurs relations :
users ⟶ 1:N ⟶ decks

decks ⟶ 1:N ⟶ cards

users ⟶ 1:N ⟶ reviews

cards ⟶ 1:N ⟶ reviews

cards ⟷ N:N ⟷ tags (via table card_tags)

------------------------------------------------------------
🔗 Requêtes REST typiques (mock json-server ou futur backend)

🔍 Utilisateurs & Decks
GET /users : liste des utilisateurs

GET /users/:id : infos d'un utilisateur

GET /decks?userId=1 : decks créés par l'utilisateur 1

📚 Decks & Cartes
GET /decks : tous les decks

GET /decks/:id/cards ou GET /cards?deckId=1 : cartes d'un deck

POST /decks : création d’un nouveau deck

PUT /decks/:id : mise à jour d’un deck

DELETE /decks/:id : suppression d’un deck

🃏 Cartes & Révisions
GET /cards/:id : détail d’une carte

GET /cards?status=à%20revoir : filtrage des cartes

POST /cards : ajout d’une carte

PUT /cards/:id : modification d’une carte

DELETE /cards/:id : suppression d’une carte

📈 Reviews & Statistiques
GET /reviews?userId=1 : toutes les révisions d’un utilisateur

GET /reviews?cardId=15 : historique de révision d’une carte

POST /reviews : ajouter une review

------------------------------------------------------------
🧾 Documentation des types de données

📄 Table users
id : int → Clé primaire, auto-incrémentée

username : varchar → Unique, NOT NULL

email : varchar → Unique, NOT NULL

password : text → Hashé, NOT NULL

created_at : datetime

updated_at : datetime

📄 Table decks
id : int → Clé primaire, auto-incrémentée

name : varchar → NOT NULL

description : text

user_id : int → Foreign Key vers users.id

created_at : datetime

updated_at : datetime

📄 Table cards
id : int → Clé primaire, auto-incrémentée

question : text → NOT NULL

answer : text → NOT NULL

deck_id : int → Foreign Key vers decks.id

status : enum → 'révisée', 'à revoir', 'acquise'

created_at : datetime

updated_at : datetime

last_reviewed_at : datetime

📄 Table reviews
id : int → Clé primaire, auto-incrémentée

user_id : int → Foreign Key vers users.id

card_id : int → Foreign Key vers cards.id

rating : enum → 'correct' ou 'incorrect'

timestamp : datetime






