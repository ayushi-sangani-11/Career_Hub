# Smart CareerHub — AI-Powered Career, Resume & Job Recommendation Platform

**Smart CareerHub** is a production-grade, full-stack web application designed for college students, fresh graduates, and job seekers to assess career readiness, parse PDF resumes using Python NLP, identify skill gaps for target roles, view transparent job match scores, and receive personalized career recommendations.

---

## 🚀 Key Features

### 🎓 Student Features
- **Professional Career Profile**: Manage personal details, academic background, target role goals, and skills.
- **Python NLP Resume Analysis**: PDF text extraction, technical & soft skill detection, section validation, and quality score calculation (0–100).
- **Skill Gap Engine**: Benchmarks candidate skills against target career role matrices (Full Stack, Python AI, DevOps, Data Analyst, Cloud Engineer, UI/UX).
- **Smart Job Matching**: Transparent compatibility percentage calculation (e.g. 94% Match) with breakdown of matched vs. missing prerequisites.
- **AI Recommendations**: Personalized job recommendation ranking powered by skill matching and user preference algorithms.
- **Application Tracker**: Visual hiring pipeline tracking (`Applied` → `Under Review` → `Shortlisted` → `Interview` → `Selected` / `Rejected`).
- **Saved Jobs**: Bookmark job opportunities for future application.
- **Learning Recommendations**: Curated learning courses mapped directly to missing candidate skills.
- **Real-time Notifications**: Alerts for resume parsing, status updates, and job matches.

### 🛡️ Admin Features
- **Platform Analytics Dashboard**: Overview stats and Recharts visual charts for job categories, applications pipeline, and top skills.
- **User Management**: View student profiles, toggle account active/deactive status, and manage access.
- **Job Management**: Create, edit, toggle active status, and delete job postings with required & preferred skill prerequisites.
- **Skill & Course Catalog Management**: Expand the skill taxonomy catalog and publish learning resources.
- **Applications Review**: Review student job applications and update candidate hiring stage with feedback notes.

---

## 🛠️ Technology Stack

- **Frontend**: React.js, Tailwind CSS, Lucide Icons, Recharts, Axios, React Router DOM v6, Vite.
- **Backend API**: Node.js, Express.js, REST API, JWT Authentication, bcryptjs, Multer file upload handler.
- **Database**: MongoDB & Mongoose ORM (Supports MongoDB Atlas / local MongoDB, with built-in Javascript NLP fallback handling).
- **Python AI Microservice**: Python 3.14, FastAPI, Uvicorn, PyPDF, Regex NLP skill extraction engine, TF-IDF cosine similarity job matching.

---

## 📐 Application Architecture

```
React Frontend (Vite on Port 3000)
       ↓  (HTTP / REST API)
Node.js + Express API (Port 5000)  ←→  MongoDB Database
       ↓  (HTTP Microservice Call)
Python FastAPI Service (Port 8000) (PDF Parsing / NLP / Skill Gap Engine)
```

---

## 🔑 Demo Login Credentials (Seed Data)

After running the database seed script (`npm run seed` inside `backend/`), you can log in with:

| Role | Email | Password |
| :--- | :--- | :--- |
| **Student** | `student@smartcareerhub.com` | `student123` |
| **Admin** | `admin@smartcareerhub.com` | `admin123` |

---

## 💻 Quick Start & Setup Instructions

### 1. Start Python AI Microservice (`python-ai/`)

```bash
cd python-ai
python -m pip install -r requirements.txt
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
*Python AI Service will run on `http://127.0.0.1:8000`*

### 2. Start Node.js Express Backend (`backend/`)

```bash
cd backend
npm install
npm run seed     # Populate database with realistic demo jobs, skills, courses, student & admin accounts
npm start        # Starts server on port 5000
```
*Node REST API will run on `http://localhost:5000`*

### 3. Start React Frontend (`frontend/`)

```bash
cd frontend
npm install
npm run dev
```
*React app will run on `http://localhost:3000`*

---

## 📡 API Endpoint Overview

### Auth Endpoints
- `POST /api/auth/register` — Register student account
- `POST /api/auth/login` — Login user (Returns JWT Token & User object)
- `GET /api/auth/me` — Fetch authenticated user details

### Resume Endpoints
- `POST /api/resumes/upload` — Upload PDF resume & trigger Python NLP analysis
- `GET /api/resumes/my-resume` — Get parsed resume analysis data
- `DELETE /api/resumes/my-resume` — Delete uploaded resume

### Job & Recommendation Endpoints
- `GET /api/jobs` — Search & filter jobs by title, location, type, experience, skill
- `GET /api/jobs/:id` — Get detailed job specification & candidate match score
- `GET /api/jobs/recommendations` — Fetch AI ranked job recommendations
- `POST /api/jobs` — Create new job posting (Admin)

### Application Endpoints
- `POST /api/applications/apply` — Apply for a job position
- `GET /api/applications/my-applications` — Get candidate application tracker timeline
- `GET /api/applications/admin/all` — Fetch all candidate applications (Admin)
- `PUT /api/applications/admin/:id/status` — Update application hiring stage (Admin)

---

## 🌟 Future Scope
- AI Mock Interview Assistant
- Automatic ATS Resume Formatting Tool
- Recruiter Portal & Direct Candidate Messaging
