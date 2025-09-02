
# Insurance Management App

A full-stack web application for managing insurance operations, built with **FastAPI** (backend) and **React** (frontend).

---

## 🚀 Project Overview
This app provides modules for:
- Accounts Payable
- Product & Receivable Management
- Claims, Loans, Policies, and more

---

## 📦 Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL (or compatible database)

---

## 🛠️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/insurance-app.git
cd insurance-app
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts ctivate`
pip install -r ../requirements.txt
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
npm start
```

---

## 🔐 Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost/dbname
FRONTEND_URL=http://localhost:3000
```

---

## 📁 Folder Structure
```
insurance-app/
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── templates/
│   └── static/
├── frontend/
│   ├── App.jsx
│   ├── components/
│   └── pages/
├── .env
├── requirements.txt
├── render.yaml
├── .gitignore
└── README.md
```

---

## 🚢 Deployment on Render
Render uses `render.yaml` to configure services.

### Backend Service
- Type: `web`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`

### Frontend Service
- Type: `web`
- Start Command: `npm start`
- Static Publish Path: `build`

---

## 📬 Contact
For questions or support, reach out to [your-email@example.com](mailto:your-email@example.com)

"# InsuranceAfricaApp" 
