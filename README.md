# 🚀 Automatisation des Tests - Automation Exercise

## 📌 Présentation

Ce projet permet d'automatiser les tests du site [Automation Exercise](http://automationexercise.com) en utilisant **Selenium**. Il vise à tester le processus d'achat et la gestion du panier. 🛒🛍️

L'énoncé initial se trouve dans le fichier [enonce.md](./enonce.md)

---

## 📂 Structure du Projet

📁 **tests/**  (Dossier contenant les implémentations des tests Python avec Selenium)
📁 **tests/features/** → Contient les fichiers **Gherkin** décrivant les scénarios de test.  
📁 **utils/** → Fichiers utilitaires et fonctions d'aide pour l'exécution des tests.  
📄 **README.md** → Ce fichier d'explication du projet. 📖

---

## ⚙️ Prérequis

✔ **Python** 🐍  
✔ **Selenium** 🌐  
✔ **WebDriver** compatible avec votre navigateur (ex: **ChromeDriver** pour Google Chrome) 🖥️

---

## 🔧 Installation

Avant d'exécuter les tests, suivez les instructions du fichier [installation.md](./installation.md)

## ▶️ Exécution des Tests

👉 **Lancer tous les scénarios Gherkin avec** 🎯
```bash
pytest tests/test_elements.py --html=report.html
```

👉 **Exécuter un test spécifique** 🎯
```bash
pytest tests/test_elements.py --gherkin-terminal-reporter --html=report.html -k "Test_The_Radio_Button"
```

---

## 📋 Scénarios de Test

```Gherkin
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
    
  Scenario: Search and Manage Cart on Automation Exercise as logged in user
	  Given I search for "Product A" 
	  When I add the product to the cart 
	  And I log into my account 
	  Then I can delete all previous added products from the cart
```

---

## 📊 📑 Rapport des Tests

Après exécution, un rapport détaillé des résultats est généré. 📈  
Vous pouvez le retrouver dans le fichier **report.html** après chaque test.

---