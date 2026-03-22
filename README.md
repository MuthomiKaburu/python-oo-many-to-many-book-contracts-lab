# 📚 Many-to-Many Relationships Lab: Book Contracts

## 🧾 Overview

This project demonstrates how to implement a **many-to-many relationship** in Python using object-oriented programming (OOP).

The system models relationships between:

* **Authors**
* **Books**
* **Contracts** (intermediary)

An author can have multiple books, and a book can have multiple authors. This relationship is managed through the **Contract** class, which also stores additional data such as contract date and royalties.

---

## 🎯 Objectives

* Understand and implement many-to-many relationships
* Use an intermediary class to connect models
* Practice Python OOP concepts:

  * Classes and instances
  * Class attributes
  * Instance methods
  * Properties and validation
* Build a structured and scalable model

---

## 🧠 System Design

### 📘 Classes and Responsibilities

#### 1. Author

Represents a book author.

**Attributes:**

* `name` (string)
* `all` (class list storing all Author instances)

**Methods:**

* `contracts()` → returns all contracts for the author
* `books()` → returns all books associated with the author
* `sign_contracts(book, date, royalties)` → creates a new contract
* `total_royalties()` → calculates total earnings from contracts

---

#### 2. Book

Represents a book.

**Attributes:**

* `title` (string)
* `all` (class list storing all Book instances)

**Methods:**

* `contracts()` → returns all contracts for the book
* `authors()` → returns all authors associated with the book

---

#### 3. Contract

Acts as the **join model** between Author and Book.

**Attributes:**

* `author` (Author instance)
* `book` (Book instance)
* `date` (string)
* `royalties` (integer)
* `all` (class list storing all Contract instances)

**Methods:**

* `contracts_by_date(date)` → returns all contracts for a specific date

**Validations (via properties):**

* `author` must be an Author instance
* `book` must be a Book instance
* `date` must be a string
* `royalties` must be an integer

---

## 🔗 Relationship Structure

```
Author  ←→  Contract  ←→  Book
```

* One Author → many Contracts
* One Book → many Contracts
* Contracts link Authors and Books

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Open the project in your preferred IDE (VS Code recommended)

3. Run the Python file:

```bash
python your_file_name.py
```

---

## 🧪 Example Usage

```python
a1 = Author("Alice")
a2 = Author("Bob")

b1 = Book("Data Science")
b2 = Book("Machine Learning")

a1.sign_contracts(b1, "2026-03-20", 1000)
a1.sign_contracts(b2, "2026-03-21", 500)
a2.sign_contracts(b1, "2026-03-20", 700)

print(a1.books())
print(b1.authors())
print(a1.total_royalties())
print(Contract.contracts_by_date("2026-03-20"))
```

