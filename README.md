# Python Virtual Environments & PEP8

This repository is a personal learning space focused on **Python best practices**, specifically:

* Working with **virtual environments**
* Writing clean, readable code following **PEP8**
* Keeping Python projects organized and portable across machines

The goal is to separate **conceptual notes** (kept externally) from **executable code**, ensuring everything here can be run, tested, and reused.

---

## What You’ll Find Here

* Practical examples using Python virtual environments.
* Code written and formatted according to PEP8 standards.
* Small scripts and exercises to reinforce best practices.
* A clean and scalable folder structure for learning and projects.

---

## Virtual Environments

All examples assume the use of a virtual environment to isolate dependencies per project.

### 1. Create a virtual environment
`python -m venv venv`

### 2. Activate it
* **Windows:**
  `.\venv\Scripts\activate`
* **macOS / Linux:**
  `source venv/bin/activate`

### 3. Deactivate
`deactivate`

> **Note:** The `venv/` folder is ignored via `.gitignore` and should never be committed to the repository.

---

## PEP8 Guidelines Applied

This repository follows Python’s official style guide (**PEP8**) to ensure professional code quality:

* **Meaningful Names:** Using `snake_case` for variables and functions.
* **Indentation:** Consistent use of 4 spaces per level.
* **Line Length:** Awareness of line length for better readability.
* **Logic Separation:** Clear use of blank lines and modular functions.
* **Clean Refactoring:** Ability to read and refactor non-compliant code.

---

## Repository Philosophy

* **Executable Code:** GitHub stores runnable examples, not just text.
* **Topic-Based:** Each folder represents a specific Python concept.
* **Focus:** Files are small, documented, and easy to study.
* **Portability:** Designed to be cloned and run on any machine quickly.

---

## How to Use This Repo

1. **Clone the repository:** `git clone https://github.com/your-username/python-virtualenvs-pep8.git`
2. **Navigate to the folder:** `cd python-virtualenvs-pep8`
3. **Setup your environment:** Create and activate your `venv` as shown in the section above.
4. **Explore:** Modify and experiment freely with the scripts.

---

## Future Additions

* More examples on environment management.
* Automation scripts and mini-projects.
* Tooling for linting and formatting (Flake8, Black).

---

## Author

**Daniel**
*Software Engineering Student*

---
