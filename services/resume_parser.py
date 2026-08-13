"""
Resume Parser and ATS Heuristic Analyzer for CareerAI.
Parses uploaded PDF resumes, extracts sections, detects keywords, and computes ATS match scores.
"""

import os
import re
from typing import Dict, Any, List
from pypdf import PdfReader
from services.mock_data import ROLE_TAXONOMY

# Skill taxonomy keywords for extraction
ALL_TECH_KEYWORDS = {
    "python", "flask", "django", "fastapi", "javascript", "typescript", "html", "html5", "css", "css3",
    "react", "vue", "node.js", "nodejs", "c", "c++", "embedded c", "esp32", "arduino", "iot", "digital twin",
    "sql", "sqlite", "postgresql", "mysql", "mongodb", "git", "github", "docker", "opencv", "computer vision",
    "machine learning", "deep learning", "ai", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "rest", "restful api", "api", "linux", "aws", "gcp", "azure", "ci/cd", "data structures", "algorithms",
    "oop", "object-oriented programming", "mqtt", "websockets", "i2c", "spi", "uart", "microcontroller",
    "power management", "predictive maintenance", "anomaly detection", "google sheets api", "face recognition"
}

ALL_SOFT_KEYWORDS = {
    "communication", "teamwork", "leadership", "problem solving", "analytical thinking", "adaptability",
    "time management", "critical thinking", "collaboration", "agile", "presentation", "troubleshooting",
    "mentorship", "creativity", "attention to detail", "curiosity", "self-motivated"
}

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract raw text from a PDF file using pypdf."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text.strip()

def analyze_resume_text(text: str, target_role: str = "Software Developer", filename: str = "resume.pdf") -> Dict[str, Any]:
    """Analyze resume text for ATS compatibility, keyword density, and role alignment."""
    if not text or len(text.strip()) < 50:
        # Fallback to realistic demo analysis if file is empty or demo mode
        return get_demo_resume_analysis(target_role)

    text_lower = text.lower()
    words = re.findall(r'\b[a-zA-Z0-9\+\#\.\-]+\b', text_lower)
    word_count = len(words)

    # 1. Detect Contact Info
    has_email = bool(re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text))
    has_phone = bool(re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text))
    has_linkedin = "linkedin.com" in text_lower
    has_github = "github.com" in text_lower

    # 2. Section Headings Check
    sections = {
        "education": bool(re.search(r'\b(education|academic|b\.tech|degree|university|college)\b', text_lower)),
        "skills": bool(re.search(r'\b(skills|technical skills|technologies|competencies|proficiencies)\b', text_lower)),
        "projects": bool(re.search(r'\b(projects|personal projects|academic projects|key projects)\b', text_lower)),
        "experience": bool(re.search(r'\b(experience|internships|work experience|employment)\b', text_lower)),
        "certifications": bool(re.search(r'\b(certifications|certificates|licenses|courses)\b', text_lower)),
    }

    # 3. Detect Technical Skills
    detected_tech = []
    for skill in ALL_TECH_KEYWORDS:
        # Match whole words or compound terms
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            detected_tech.append(skill.title() if len(skill) > 3 else skill.upper())

    # 4. Detect Soft Skills
    detected_soft = []
    for skill in ALL_SOFT_KEYWORDS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            detected_soft.append(skill.title())

    # 5. Role Alignment & Missing Keywords
    role_info = ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Software Developer"])
    core_skills = role_info.get("core_skills", [])

    matched_core = []
    missing_core = []
    for cs in core_skills:
        skill_name = cs["name"].lower()
        matched = False
        for piece in re.split(r'[/,&()]', skill_name):
            piece_clean = piece.strip()
            if piece_clean and piece_clean in text_lower:
                matched = True
                break
        if matched:
            matched_core.append(cs["name"])
        else:
            missing_core.append(cs["name"])

    # 6. Compute ATS & Sub-Scores
    section_score = sum(18 for k, v in sections.items() if v)  # up to 90
    contact_score = (10 if has_email else 0) + (10 if has_phone else 0) + (5 if has_github or has_linkedin else 0)  # up to 25
    tech_density_score = min(len(detected_tech) * 5, 30)
    keyword_match_pct = int((len(matched_core) / max(len(core_skills), 1)) * 100)
    
    # Calculate Overall ATS Score (0-100)
    raw_ats = 40 + (section_score * 0.25) + (contact_score * 0.15) + (keyword_match_pct * 0.25) + (tech_density_score * 0.35)
    ats_score = int(max(min(raw_ats, 98), 50))

    formatting_score = 92 if (has_email and sections["education"] and sections["skills"]) else 76

    # 7. Actionable Recommendations
    recommendations = []
    if missing_core:
        top_missing = ", ".join(missing_core[:3])
        recommendations.append(f"Incorporate high-impact target keywords for {target_role}: {top_missing}.")
    if not sections["certifications"]:
        recommendations.append("Add a dedicated 'Certifications & Courses' section to highlight verified LinkedIn learning.")
    if not (has_github and has_linkedin):
        recommendations.append("Include clickable hyperlinks to both your GitHub repository and LinkedIn profile.")
    if word_count < 250:
        recommendations.append("Expand project bullet points using the Action-Verb + Metric + Result (STAR) framework.")
    else:
        recommendations.append("Maintain clear bullet formatting and quantify project metrics (e.g., 'reduced latency by 40%').")

    return {
        "filename": filename,
        "target_role": target_role,
        "is_demo": False,
        "ats_score": ats_score,
        "keyword_match_pct": keyword_match_pct,
        "formatting_score": formatting_score,
        "word_count": word_count,
        "detected_tech_skills": sorted(list(set(detected_tech)))[:15],
        "detected_soft_skills": sorted(list(set(detected_soft)))[:8],
        "matched_keywords": matched_core,
        "missing_keywords": missing_core,
        "sections_detected": sections,
        "contact_info": {
            "has_email": has_email,
            "has_phone": has_phone,
            "has_linkedin": has_linkedin,
            "has_github": has_github
        },
        "recommendations": recommendations,
        "role_category": role_info.get("category", "Software Engineering")
    }

def get_demo_resume_analysis(target_role: str = "Software Developer") -> Dict[str, Any]:
    """Generate a realistic demonstration resume analysis."""
    role_info = ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Software Developer"])
    core_skills = role_info.get("core_skills", [])
    
    matched = [cs["name"] for cs in core_skills[:4]]
    missing = [cs["name"] for cs in core_skills[4:]] if len(core_skills) > 4 else ["Cloud Deployment (AWS/GCP)", "Docker Containerization"]

    return {
        "filename": "Annareddy_Naveen_Kumar_Reddy_Resume.pdf",
        "target_role": target_role,
        "is_demo": True,
        "ats_score": 88,
        "keyword_match_pct": 82,
        "formatting_score": 94,
        "word_count": 485,
        "detected_tech_skills": [
            "Python", "Flask", "OpenCV", "JavaScript", "HTML5", "CSS3", "SQLite",
            "ESP32", "IoT", "Digital Twin", "Git & GitHub", "Google Sheets API"
        ],
        "detected_soft_skills": [
            "Problem Solving", "Analytical Thinking", "Troubleshooting",
            "Collaboration", "Communication", "Time Management"
        ],
        "matched_keywords": matched,
        "missing_keywords": missing,
        "sections_detected": {
            "education": True,
            "skills": True,
            "projects": True,
            "experience": True,
            "certifications": True
        },
        "contact_info": {
            "has_email": True,
            "has_phone": True,
            "has_linkedin": True,
            "has_github": True
        },
        "recommendations": [
            f"Add target keywords such as '{missing[0] if missing else 'System Design'}' in project descriptions to boost ATS rank.",
            "Quantify project achievements with operational metrics (e.g., 'Processed 30+ frames/sec in face detection').",
            "Highlight verified LinkedIn certifications directly under a focused Credentials section."
        ],
        "role_category": role_info.get("category", "Software Engineering")
    }
