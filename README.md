# CareerAI — AI Interview & Career Coach

<p align="center">
  <img src="static/images/naveen_profile.jpg" alt="Annareddy Naveen Kumar Reddy" width="120" style="border-radius: 50%; border: 3px solid #38bdf8;" />
</p>

<p align="center">
  <strong>Engineered by Annareddy Naveen Kumar Reddy</strong><br>
  <em>3rd Year B.Tech in Electronics & Communication Engineering (ECE) • Mohan Babu University</em><br>
  Student ID: <code>25301A030039</code> • Kadapa District, Andhra Pradesh, India
</p>

<p align="center">
  <a href="https://github.com/annareddy-naveen-kumar-reddy"><img src="https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github" alt="GitHub" /></a>
  <a href="https://www.linkedin.com/in/annareddy-naveen-kumar-reddy-037343377/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin" alt="LinkedIn" /></a>
  <a href="https://annareddy-naveen-kumar-reddy.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-Live_Site-38bdf8?style=flat" alt="Portfolio" /></a>
  <a href="mailto:naveenkumarreddyannareddy@gmail.com"><img src="https://img.shields.io/badge/Email-Contact_Me-EA4335?style=flat&logo=gmail" alt="Email" /></a>
</p>

---

## 🚀 Overview

**CareerAI** is a personal AI-powered career preparation platform designed to help students and engineering candidates practice technical & HR mock interviews, audit resumes for ATS compatibility, analyze skill gaps, and match with competitive software, IoT, and AI job roles.

---

## 🌟 Key Features & Architecture

1. **AI Mock Interview Room (`/interview`)**:
   - Dynamic question generation across 7 role tracks (Software Developer, Python Developer, Web Developer, Data Analyst, AI/ML Beginner, ECE Engineer, Custom Role).
   - **Web Speech API Speech-to-Text**: Live voice answering with real-time waveform visualization.
   - Granular evaluation rubric: Overall Score, Technical Depth, Communication, Confidence, Relevance, and Answer Quality.
   - Actionable feedback: *"What You Did Well"*, *"What You Missed"*, *"How To Improve"*, and *"Exemplary Model Answer"*.
   - Final comprehensive interview scorecard automatically logged to SQLite database.

2. **Resume ATS Analyzer (`/resume`)**:
   - PDF resume upload with `pypdf` parsing and text-paste analysis.
   - Overall ATS Compatibility Gauge, keyword match percentage, and formatting score.
   - Detected technical & soft skill chips with missing target keywords.
   - Standard section verification checklist (Education, Skills, Projects, Experience, Certifications).

3. **Career Readiness Dashboard (`/dashboard`)**:
   - Candidate Placement Readiness Index (88%).
   - **Interactive SVG Line Chart** tracking interview performance trajectory over time.
   - **5-Axis Radar Skill Polygon** (Software Dev, Python/Flask, ECE/IoT, AI/Vision, Communication).
   - Recent interview history and actionable milestone recommendations.

4. **Skill Gap Analyzer (`/skills`) & Job Role Matcher (`/role-matcher`)**:
   - Priority-tagged skill competency matrices (`High Priority`, `Medium`, `On Track`).
   - Weighted multi-role compatibility matching engine.

5. **Verified Projects Showcase (`/projects`)**:
   - ⭐ **SmartLabTwinAI (Featured Flagship Project)**: *"An AI-Powered Digital Twin for Intelligent Laboratory Monitoring, Predictive Maintenance, and Smart Energy Management"*. Includes interactive real-time IoT telemetry simulator (Temperature, Humidity, Voltage, Current draw) with stress-test trigger.
   - 🚧 **AI Smart Attendance System (In Active Development • 75% Complete)**: *"Computer Vision-Based Automated Attendance Logging with Cloud Synchronization"*. Includes simulated OpenCV face detection logs and Google Sheets sync.

6. **Profile Customizer (`/profile`) & Verified Credentials (`/certifications`)**:
   - Direct integration to LinkedIn certifications.
   - Dynamic SQLite-backed skill management (Add/Delete/Proficiency).

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Flask, SQLite3, `pypdf`, `python-dotenv`, `requests`
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism, Dark/Light Themes), Modern JavaScript (ES6+), Web Speech API
- **AI Architecture**: Unified provider interface supporting Google Gemini API, OpenAI API, and intelligent built-in deterministic Demo Engine.

---

## 💻 Local Setup & Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/annareddy-naveen-kumar-reddy/careerai.git
   cd careerai
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   ```bash
   cp .env.example .env
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Open in Browser**:
   - **Local machine**: `http://localhost:5000` or `http://127.0.0.1:5000`
   - **Mobile / Local Network**: `http://<YOUR_LOCAL_IP>:5000`

---

## 🧪 Automated Testing

Run the full test suite verifying all 12 page routes and REST API endpoints:
```bash
python test_suite.py
```

---

## 📜 License

Created by **Annareddy Naveen Kumar Reddy**. All rights reserved.
