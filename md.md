Voici votre **README.md** mis à jour pour refléter l'utilisation du **Page Object Model (POM)** et la nouvelle structure du projet.  

---

# 🚀 Automatisation des Tests - Automation Exercise

## 📌 Présentation

Ce projet permet d'automatiser les tests du site [Automation Exercise](http://automationexercise.com) en utilisant **Selenium** avec l'approche **Page Object Model (POM)**.  
L'objectif est de tester le **processus d'achat**, la **gestion du panier**, et la **création de compte** pour finaliser une commande et télécharger une facture. 🛒🛍️  

🔹 **L'énoncé initial** se trouve dans le fichier [enonce.md](./enonce.md)  

---

## 🎯 **Pourquoi le choix du Page Object Model (POM) ?**
L'approche **POM (Page Object Model)** a été adoptée pour **rendre les tests plus modulaires, maintenables et réutilisables**.  
Chaque page du site est représentée par une **classe dédiée**, ce qui permet :  
✔ Une **séparation claire** entre la logique des tests et la gestion des éléments de l'interface.  
✔ Une **réutilisation des méthodes** entre plusieurs scénarios.  
✔ Une **maintenance plus facile** en cas de changement de l'interface du site.  

---

## 📂 **Structure du Projet**

```
📁 fixtures/         → Contient les fixtures et générateurs de données (ex: emails, mots de passe aléatoires).
📁 pages/           → Implémentation du modèle Page Object pour chaque page du site.
📁 tests/           → Contient les tests automatisés utilisant les pages du POM.
📁 tests/features/  → Contient les scénarios Gherkin pour pytest-bdd.
📄 README.md        → Documentation du projet.
```

### 🔹 **Détails des dossiers**
| Dossier | Description |
|---------|------------|
| **`fixtures/`** | Contient les **fixtures Pytest** et les générateurs de **données aléatoires** (ex: `random_email.py`, `password_generator.py`). |
| **`pages/`** | Chaque page du site est implémentée comme une **classe POM** (ex: `HomePage.py`, `SignupPage.py`). |
| **`tests/`** | Contient les fichiers de **tests automatisés** (ex: `test_add_product.py`). |
| **`tests/features/`** | Fichiers **Gherkin** décrivant les scénarios de test. |

---

## ⚙️ **Prérequis**
✔ **Python** 🐍  
✔ **Selenium** 🌐  
✔ **WebDriver** compatible avec votre navigateur (ex: **ChromeDriver** pour Google Chrome) 🖥️  
✔ **Pytest & pytest-bdd**  

📌 **Installation des dépendances** :
```sh
pip install -r requirements.txt
```

---

## ▶️ **Exécution des Tests**

👉 **Lancer tous les scénarios Gherkin** 🎯
```sh
pytest tests/ --html=report.html
```

👉 **Exécuter un test spécifique** 🎯
```sh
pytest tests/test_add_product.py --gherkin-terminal-reporter --html=report.html -k "test_add_product_to_cart"
```

---

## 📋 **Scénarios de Test**
Le projet suit la méthodologie **BDD (Behavior Driven Development)** avec des scénarios écrits en **Gherkin**.

### **🛒 Scénario : Création d’un compte et finalisation de la commande**
```gherkin
Feature: Purchase and Cart Management on Automation Exercise 
  As a user of Automation Exercise
  I want to search for products, manage my cart, and complete a purchase
  So that I can finalize my order and download my invoice

  Scenario: Create an account to complete an order and download the invoice 
    Given I add products to the cart 
    When I create an account 
    And I am logged in
    Then I can finalize the purchase
    And I can download the invoice of the purchase successfully  
```

### **🔎 Scénario : Recherche et gestion du panier**
```gherkin
  Scenario: Search and Manage Cart on Automation Exercise as logged in user
    Given I search for "Product A" 
    When I add the product to the cart 
    And I log into my account 
    Then I can delete all previous added products from the cart
```

---

## 📊 **📑 Rapport des Tests**
Après chaque exécution, un **rapport HTML détaillé** est généré. 📈  
Vous pouvez le consulter dans **`report.html`** après chaque test.

📌 **Exemple de commande pour générer un rapport** :
```sh
pytest tests/ --html=report.html --self-contained-html
```

---

## 🔥 **Améliorations futures**
🚀 **Ajout de nouveaux scénarios** (ex: Paiement, Validation de livraison).  
🔍 **Intégration avec CI/CD** pour exécuter les tests automatiquement.  
📊 **Génération de rapports Allure** pour une meilleure visualisation des résultats.  

---

💡 **Auteur :** [Votre Nom]  
📅 **Dernière mise à jour :** [Date]  
🔗 **Site testé :** [Automation Exercise](http://automationexercise.com)  

---

🚀 **Maintenant, vos tests sont structurés en POM et alignés avec la méthodologie BDD !** 🚀