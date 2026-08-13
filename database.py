import sqlite3
import json
import os
from datetime import datetime
from config import Config

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # User Profile Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_id TEXT,
        university TEXT,
        branch TEXT,
        year TEXT,
        location TEXT,
        email TEXT,
        phone TEXT,
        github TEXT,
        linkedin TEXT,
        portfolio TEXT,
        bio TEXT,
        headline TEXT,
        target_role TEXT DEFAULT 'Software Developer',
        career_readiness INTEGER DEFAULT 78,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Skills Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        name TEXT NOT NULL,
        proficiency INTEGER DEFAULT 3,
        is_verified INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Projects Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        subtitle TEXT,
        description TEXT NOT NULL,
        tech_tags TEXT NOT NULL,
        features_json TEXT,
        github_url TEXT,
        demo_url TEXT,
        highlight_color TEXT DEFAULT '#38bdf8',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Certifications Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS certifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        issuer TEXT,
        issue_date TEXT,
        credential_url TEXT,
        credential_id TEXT,
        is_linkedin_synced INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Achievements Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        milestone_date TEXT,
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Interviews Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS interviews (
        id TEXT PRIMARY KEY,
        role TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        interview_type TEXT NOT NULL,
        total_questions INTEGER DEFAULT 5,
        completed_questions INTEGER DEFAULT 0,
        overall_score INTEGER DEFAULT 0,
        technical_score INTEGER DEFAULT 0,
        communication_score INTEGER DEFAULT 0,
        confidence_score INTEGER DEFAULT 0,
        relevance_score INTEGER DEFAULT 0,
        summary TEXT,
        strengths_json TEXT,
        weaknesses_json TEXT,
        recommendations_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Interview Answers Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS interview_answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        interview_id TEXT NOT NULL,
        question_number INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        user_answer TEXT,
        score INTEGER DEFAULT 0,
        tech_score INTEGER DEFAULT 0,
        comm_score INTEGER DEFAULT 0,
        confidence_score INTEGER DEFAULT 0,
        relevance_score INTEGER DEFAULT 0,
        feedback_well TEXT,
        feedback_missed TEXT,
        feedback_improve TEXT,
        better_example TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (interview_id) REFERENCES interviews(id)
    )
    ''')

    # Resume Scans Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resume_scans (
        id TEXT PRIMARY KEY,
        target_role TEXT NOT NULL,
        filename TEXT,
        ats_score INTEGER DEFAULT 0,
        keyword_match_pct INTEGER DEFAULT 0,
        skills_detected_json TEXT,
        missing_keywords_json TEXT,
        formatting_score INTEGER DEFAULT 0,
        recommendations_json TEXT,
        full_analysis_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Contact Messages Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        ip_address TEXT,
        is_read INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()

    # Seed verified initial profile if not exists
    cursor.execute('SELECT COUNT(*) as count FROM user_profile')
    if cursor.fetchone()['count'] == 0:
        cursor.execute('''
        INSERT INTO user_profile (
            name, student_id, university, branch, year, location,
            email, phone, github, linkedin, portfolio, bio, headline,
            target_role, career_readiness
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            Config.DEVELOPER_NAME,
            Config.DEVELOPER_STUDENT_ID,
            Config.DEVELOPER_UNIVERSITY,
            Config.DEVELOPER_BRANCH,
            Config.DEVELOPER_YEAR,
            Config.DEVELOPER_LOCATION,
            Config.DEVELOPER_EMAIL,
            Config.DEVELOPER_PHONE,
            Config.DEVELOPER_GITHUB,
            Config.DEVELOPER_LINKEDIN,
            Config.DEVELOPER_PORTFOLIO,
            "3rd-year Electronics and Communication Engineering student at Mohan Babu University with hands-on focus on Software Development, Artificial Intelligence, Web Technologies, IoT systems, and real-time data processing.",
            "ECE Student | AI & Web Developer | B.Tech 3rd Year",
            "Software Developer",
            82
        ))

    # Seed verified projects if empty
    cursor.execute('SELECT COUNT(*) as count FROM projects')
    if cursor.fetchone()['count'] == 0:
        cursor.execute('''
        INSERT INTO projects (
            title, subtitle, description, tech_tags, features_json, github_url, demo_url, highlight_color
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            "SmartLabTwinAI",
            "AI-Powered Digital Twin for Intelligent Laboratory Monitoring, Predictive Maintenance, and Smart Energy Management",
            "An integrated IoT and AI digital twin platform engineered to continuously monitor environmental metrics, electrical parameters, and equipment health across academic and research laboratories. Features machine learning anomaly detection for predictive maintenance and automated power optimization.",
            "ESP32, IoT, AI Anomaly Detection, Digital Twin, Predictive Maintenance, Energy Management, Python, WebSockets",
            json.dumps([
                "Real-time temperature and humidity tracking via calibrated IoT sensors",
                "Continuous voltage, current, and active power draw monitoring",
                "Machine Learning-driven anomaly classification to forecast component failures",
                "Automated alerting engine with digital twin telemetry visualization",
                "Dynamic energy management reducing idle laboratory power consumption"
            ]),
            Config.DEVELOPER_GITHUB,
            "/projects#smartlabtwinai",
            "#38bdf8"
        ))

        cursor.execute('''
        INSERT INTO projects (
            title, subtitle, description, tech_tags, features_json, github_url, demo_url, highlight_color
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            "AI Smart Attendance System",
            "Computer Vision-Based Automated Attendance Logging with Cloud Synchronization",
            "A seamless facial recognition attendance management suite developed with Python, Flask, and OpenCV. Automates student and staff verification with anti-spoofing heuristics and pushes structured real-time attendance logs directly to cloud databases and Google Sheets.",
            "Python, Flask, OpenCV, SQLite, Face Recognition, Google Sheets API, Computer Vision",
            json.dumps([
                "Real-time facial detection and 128-d feature embedding vector matching",
                "Automated attendance timestamps logged securely into local SQLite storage",
                "Live synchronization pipeline with Google Sheets for faculty access",
                "Responsive administrative dashboard for attendance reporting and verification",
                "Anti-spoofing liveness check preventing static photo bypasses"
            ]),
            Config.DEVELOPER_GITHUB,
            "/projects#attendance-system",
            "#10b981"
        ))

    # Seed skills if empty
    cursor.execute('SELECT COUNT(*) as count FROM skills')
    if cursor.fetchone()['count'] == 0:
        initial_skills = [
            ("Programming", "Python", 4, 1),
            ("Programming", "C / Embedded C", 3, 1),
            ("Programming", "JavaScript (ES6+)", 4, 1),
            ("Web Technologies", "HTML5 & CSS3", 5, 1),
            ("Web Technologies", "Flask", 4, 1),
            ("AI & Data", "OpenCV", 4, 1),
            ("AI & Data", "Machine Learning Basics", 3, 1),
            ("Hardware & IoT", "ESP32 / Microcontrollers", 4, 1),
            ("Hardware & IoT", "IoT Sensor Integration", 4, 1),
            ("Hardware & IoT", "Digital Twin Concepts", 4, 1),
            ("Database & Tools", "SQLite / SQL", 4, 1),
            ("Database & Tools", "Git & GitHub", 4, 1),
            ("Database & Tools", "Google Sheets API", 4, 1),
            ("Core Engineering", "ECE Principles & Circuit Design", 4, 1),
            ("Core Engineering", "Problem Solving & Analytical Thinking", 4, 1),
        ]
        cursor.executemany(
            'INSERT INTO skills (category, name, proficiency, is_verified) VALUES (?, ?, ?, ?)',
            initial_skills
        )

    # Seed initial mock interview for career dashboard realism if empty
    cursor.execute('SELECT COUNT(*) as count FROM interviews')
    if cursor.fetchone()['count'] == 0:
        cursor.execute('''
        INSERT INTO interviews (
            id, role, difficulty, interview_type, total_questions, completed_questions,
            overall_score, technical_score, communication_score, confidence_score, relevance_score,
            summary, strengths_json, weaknesses_json, recommendations_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            "demo-interview-001",
            "Software Developer",
            "Intermediate",
            "Technical",
            5,
            5,
            86,
            88,
            84,
            85,
            87,
            "Strong grasp of core data structures, Python object-oriented patterns, and RESTful architectures. Demonstrates clear explanation skills with structured examples.",
            json.dumps(["Clear API architectural explanations", "Effective Python data structure usage", "Structured approach to problem breakdown"]),
            json.dumps(["Could elaborate more on edge-case concurrency handling", "System scaling trade-offs"]),
            json.dumps(["Practice Distributed Systems fundamentals", "Deepen understanding of asynchronous I/O in Python"]),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
