# 🎓 Student Placement Predictor

A Machine Learning web application that predicts whether a student will get placed and their expected salary package using **KNN Classification** and **Linear Regression**.

Built with Python, Scikit-learn, and FastAPI.

---

## 🚀 Live Demo

Fill in your details → Get instant placement prediction!

---

## 🧠 ML Models Used

| Model | Purpose | Accuracy |
|-------|---------|----------|
| KNN (K=15) | Placed / Not Placed | ~90% |
| Linear Regression | Expected Salary | R² = 0.94 |

---

## 📊 Input Features

| Feature | Description |
|---------|-------------|
| CGPA | Academic performance (5.0 - 10.0) |
| Aptitude Score | Problem solving ability (0-100) |
| Communication Score | English communication (0-100) |
| Projects Done | Total projects completed |
| Internship | Internship experience (Yes/No) |

---

## 🛠️ Tech Stack

- **Language** → Python 3.12
- **ML Library** → Scikit-learn
- **API Framework** → FastAPI
- **Server** → Uvicorn
- **Frontend** → HTML, CSS
- **Data Processing** → Pandas, Numpy
- **Version Control** → Git & GitHub

---

## ⚙️ How to Run Locally

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/Pawan1093/Placement-Predictor.git
cd Placement-Predictor
```

**Step 2 — Create virtual environment:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Step 3 — Install libraries:**
```bash
pip install -r requirements.txt
```

**Step 4 — Generate dataset:**
```bash
python dataset.py
```

**Step 5 — Train models:**
```bash
python train.py
```

**Step 6 — Start server:**
```bash
uvicorn main:app --reload
```

**Step 7 — Open browser:**
```
http://localhost:8000
```

---

## 📁 Project Structure
```
Placement-Predictor/
│
├── templates/
│   └── index.html        ← Frontend UI
├── dataset.py            ← Generate student data
├── train.py              ← Train ML models
├── main.py               ← FastAPI server
├── requirements.txt      ← Required libraries
└── README.md             ← Project documentation
```

---

## 🔮 How It Works
```
User fills form
      ↓
FastAPI receives data
      ↓
KNN predicts → Placed / Not Placed
Linear Regression predicts → Expected Salary
      ↓
Result shown to user instantly!
```

---

## 👨‍💻 Author

**Pawan Pawar**
Vidyavardhini's College of Engineering & Technology (VCET)

---

## 📌 Key Learnings

- Machine Learning (KNN + Linear Regression)
- REST API development with FastAPI
- Virtual environments and dependency management
- Git branching workflow
- HTML/CSS frontend development