# 📦 Thoughtful Package Sorter

This project simulates a robotic arm used in Thoughtful's automation factory. Its goal is to dispatch packages into the correct stack (`STANDARD`, `SPECIAL`, or `REJECTED`) based on their volume and mass.

---

## 🚀 Features

- 📐 **Volume & Dimension-Based Sorting**
- ⚖️ **Mass Threshold Check**
- 📤 **Stack Decision Logic** (Standard, Special, Rejected)
- ✅ **Validation with Pydantic**
- 🔁 **Extensible OOP Design**
- 🧪 **Unit Tests with unittest**
- 🧩 **Enum-based Dispatch Categories**
- 📦 **JSON Serialization Support**

---

## 📂 Project Structure

```
.
├── sorter/
│   ├── __init__.py
│   ├── enums/
│   │   └── enums.py
│   ├── models/
│   │   └── package.py
│   ├── services/
│   │   └── dispatcher.py
├── tests/
│   └── test_package.py
├── README.md
```

---

## ⚙️ Requirements

- Python 3.10+
- `pydantic` >= 2.11.5

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

Use the `sort` function to classify a package by its dimensions and mass:

```python
from sorter.services.dispatcher import sort

result = sort(width=50, height=40, length=30, mass=10)
print(result)  # ➜ "Standard"
```

### 🧠 Sorting Rules

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³, or
  - Any dimension ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

### 🧾 Stacks

| Stack     | Criteria                           |
|-----------|------------------------------------|
| STANDARD  | Not bulky and not heavy            |
| SPECIAL   | Bulky or heavy (but not both)      |
| REJECTED  | Both bulky and heavy               |

---

## 🧪 Running Tests

Run all tests with:

```bash
python -m unittest discover -s tests
```

---

## 📤 Example (CLI / JSON)

All packages support JSON serialization via `.model_dump()`:
```python
from sorter.models.package import Package

p = Package(width=50, height=40, length=30, mass=10)
print(p.model_dump())  # JSON-friendly dict
```

---

## 📌 Future Improvements

- Add CLI interface
- API wrapper using FastAPI
- Support batch processing of packages from CSV/JSON
- Store package logs in a database

---

## 🧠 Author

Developed for Thoughtful Automation as part of the robotic logistics system.