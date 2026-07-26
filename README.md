# 🎓 Academic Tracker

Academic Tracker is a Python-based application that collects, stores, compares, and visualizes academic profile statistics from multiple academic platforms.

## ✨ Features

- 📚 Google Scholar integration
- 🆔 ORCID integration
- 📊 Academic Dashboard
- 📈 Excel Reports
- 🔄 Automatic Profile Comparison
- 💾 History Tracking
- 🗂 Modular Architecture

---

## 📁 Project Structure

```
AcademicTracker/
│
├── modules/
│   ├── scholar.py
│   ├── orcid.py
│   ├── storage.py
│   ├── compare.py
│   ├── report.py
│   ├── dashboard.py
│   └── tracker.py
│
├── data/
│   ├── scholar/
│   └── orcid/
│
├── reports/
├── dashboard/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Technologies

- Python 3
- Requests
- Scholarly
- Matplotlib
- OpenPyXL
- JSON

---

## 📊 Current Modules

| Module | Status |
|---------|--------|
| Google Scholar | ✅ |
| ORCID | ✅ |
| History Tracking | ✅ |
| Excel Reports | ✅ |
| Dashboard | ✅ |
| Comparison | ✅ |

---

## 📈 Dashboard

The application automatically generates an academic dashboard including

- Citation history
- h-index history
- i10-index history
- Article history
- ORCID works
- Academic statistics cards

---

## 📄 Reports

The application generates Excel reports containing

- Previous values
- Current values
- Difference
- Automatic highlighting

---

## 💾 Data Storage

Profile data is stored as JSON files.

```
data/
    scholar/
        latest.json
        history/

    orcid/
        latest.json
        history/
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Fatma91-math/AcademicTracker.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 🛣 Roadmap

- [x] Google Scholar
- [x] ORCID
- [x] Dashboard
- [x] Excel Reports
- [x] History Tracking
- [ ] Scopus
- [ ] Semantic Scholar
- [ ] Crossref
- [ ] PDF Reports
- [ ] Email Notifications

---

## 👩‍💻 Author

**Fatma Muslumova**

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.