"""
CareerAI — AI Interview & Career Coach
Main Flask Application and API Controller.
Created for Annareddy Naveen Kumar Reddy (3rd Year B.Tech ECE, Mohan Babu University).
"""

import os
import uuid
import json
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash

from config import Config
from database import get_db_connection, init_db
from services.ai_service import ai_service
from services.resume_parser import extract_text_from_pdf, analyze_resume_text, get_demo_resume_analysis
from services.mock_data import ROLE_TAXONOMY, QUESTION_BANK

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Ensure database tables exist
with app.app_context():
    init_db()

@app.context_processor
def inject_global_data():
    """Inject verified developer profile metadata into all templates."""
    return {
        "dev_name": Config.DEVELOPER_NAME,
        "dev_student_id": Config.DEVELOPER_STUDENT_ID,
        "dev_university": Config.DEVELOPER_UNIVERSITY,
        "dev_branch": Config.DEVELOPER_BRANCH,
        "dev_year": Config.DEVELOPER_YEAR,
        "dev_location": Config.DEVELOPER_LOCATION,
        "dev_email": Config.DEVELOPER_EMAIL,
        "dev_phone": Config.DEVELOPER_PHONE,
        "dev_github": Config.DEVELOPER_GITHUB,
        "dev_linkedin": Config.DEVELOPER_LINKEDIN,
        "dev_portfolio": Config.DEVELOPER_PORTFOLIO,
        "ai_provider_name": ai_service.get_provider_name(),
        "is_demo_mode": not ai_service.is_live_ai_available(),
        "roles_list": list(ROLE_TAXONOMY.keys())
    }

# ==========================================
# PAGE ROUTES (12 SECTIONS)
# ==========================================

@app.route('/')
def index():
    """Landing Page with Hero, Feature Highlights, Quick Stats, and Live Widget."""
    conn = get_db_connection()
    skills_count = conn.execute('SELECT COUNT(*) as c FROM skills').fetchone()['c']
    interviews_count = conn.execute('SELECT COUNT(*) as c FROM interviews').fetchone()['c']
    conn.close()

    return render_template(
        'index.html',
        active_page='home',
        skills_count=skills_count,
        interviews_count=interviews_count
    )

@app.route('/interview')
def interview():
    """AI Mock Interview suite."""
    return render_template('interview.html', active_page='interview', roles=ROLE_TAXONOMY)

@app.route('/resume')
def resume():
    """AI Resume Analyzer & ATS Optimizer."""
    return render_template('resume.html', active_page='resume', roles=ROLE_TAXONOMY)

@app.route('/dashboard')
def dashboard():
    """Career Readiness Analytics Dashboard."""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM user_profile LIMIT 1').fetchone()
    recent_interviews = conn.execute('SELECT * FROM interviews ORDER BY created_at DESC LIMIT 5').fetchall()
    recent_scans = conn.execute('SELECT * FROM resume_scans ORDER BY created_at DESC LIMIT 5').fetchall()
    skills = conn.execute('SELECT * FROM skills ORDER BY category, name').fetchall()
    conn.close()

    return render_template(
        'dashboard.html',
        active_page='dashboard',
        user=user,
        recent_interviews=recent_interviews,
        recent_scans=recent_scans,
        skills=skills
    )

@app.route('/skills')
def skill_gap():
    """Skill Gap Analyzer & Career Roadmaps."""
    return render_template('skill_gap.html', active_page='skills', roles=ROLE_TAXONOMY)

@app.route('/role-matcher')
def role_matcher():
    """Job Role Matcher & Readiness Matrix."""
    return render_template('role_matcher.html', active_page='role-matcher', roles=ROLE_TAXONOMY)

@app.route('/projects')
def projects():
    """Projects Showcase (SmartLabTwinAI & AI Smart Attendance System)."""
    conn = get_db_connection()
    db_projects = conn.execute('SELECT * FROM projects ORDER BY id ASC').fetchall()
    conn.close()
    return render_template('projects.html', active_page='projects', projects=db_projects)

@app.route('/about')
def about():
    """About Developer (Annareddy Naveen Kumar Reddy)."""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM user_profile LIMIT 1').fetchone()
    conn.close()
    return render_template('about.html', active_page='about', user=user)

@app.route('/certifications')
def certifications():
    """Certifications & Learning Hub with LinkedIn Verification."""
    conn = get_db_connection()
    certs = conn.execute('SELECT * FROM certifications ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('certifications.html', active_page='certifications', certifications=certs)

@app.route('/achievements')
def achievements():
    """Achievements & Milestones Timeline."""
    conn = get_db_connection()
    achieve_list = conn.execute('SELECT * FROM achievements ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('achievements.html', active_page='achievements', achievements=achieve_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page & Message Submission."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('Please complete all required fields.', 'error')
            return redirect(url_for('contact'))

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO contact_messages (name, email, message, ip_address) VALUES (?, ?, ?, ?)',
            (name, email, message, request.remote_addr)
        )
        conn.commit()
        conn.close()

        flash('Thank you for reaching out! Your message has been received securely.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact')

@app.route('/profile')
def profile():
    """User Profile & Editable Skills Hub."""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM user_profile LIMIT 1').fetchone()
    skills = conn.execute('SELECT * FROM skills ORDER BY category, name').fetchall()
    certs = conn.execute('SELECT * FROM certifications ORDER BY created_at DESC').fetchall()
    achieve_list = conn.execute('SELECT * FROM achievements ORDER BY created_at DESC').fetchall()
    conn.close()

    return render_template(
        'profile.html',
        active_page='profile',
        user=user,
        skills=skills,
        certifications=certs,
        achievements=achieve_list
    )


# ==========================================
# REST API ENDPOINTS
# ==========================================

@app.route('/api/status', methods=['GET'])
def api_status():
    """Check AI engine status and system configuration."""
    return jsonify({
        "status": "online",
        "provider": ai_service.get_provider_name(),
        "is_demo_mode": not ai_service.is_live_ai_available(),
        "platform": "CareerAI — AI Interview & Career Coach",
        "developer": Config.DEVELOPER_NAME
    })

@app.route('/api/interview/start', methods=['POST'])
def api_interview_start():
    """Initialize a new mock interview session."""
    data = request.get_json() or {}
    role = data.get('role', 'Software Developer')
    difficulty = data.get('difficulty', 'Intermediate')
    interview_type = data.get('interview_type', 'Technical')
    num_questions = int(data.get('count', 5))

    # Generate or fetch questions
    questions = ai_service.get_interview_questions(role, difficulty, interview_type, count=num_questions)
    interview_id = f"int-{uuid.uuid4().hex[:8]}"

    # Save initial record to DB
    conn = get_db_connection()
    conn.execute('''
    INSERT INTO interviews (
        id, role, difficulty, interview_type, total_questions, completed_questions, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        interview_id, role, difficulty, interview_type, len(questions), 0,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()

    return jsonify({
        "interview_id": interview_id,
        "role": role,
        "difficulty": difficulty,
        "interview_type": interview_type,
        "total_questions": len(questions),
        "questions": questions
    })

@app.route('/api/interview/evaluate', methods=['POST'])
def api_interview_evaluate():
    """Evaluate a single question's answer dynamically."""
    data = request.get_json() or {}
    interview_id = data.get('interview_id')
    question_number = int(data.get('question_number', 1))
    question_text = data.get('question_text', '')
    user_answer = data.get('user_answer', '')
    role = data.get('role', 'Software Developer')
    difficulty = data.get('difficulty', 'Intermediate')

    # Evaluate answer via AI Service
    evaluation = ai_service.evaluate_interview_answer(role, difficulty, question_text, user_answer)

    # Save answer to DB
    conn = get_db_connection()
    conn.execute('''
    INSERT INTO interview_answers (
        interview_id, question_number, question_text, user_answer,
        score, tech_score, comm_score, confidence_score, relevance_score,
        feedback_well, feedback_missed, feedback_improve, better_example
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        interview_id, question_number, question_text, user_answer,
        evaluation.get('overall_score', 70),
        evaluation.get('technical_score', 70),
        evaluation.get('communication_score', 70),
        evaluation.get('confidence_score', 70),
        evaluation.get('relevance_score', 70),
        evaluation.get('feedback_well', ''),
        evaluation.get('feedback_missed', ''),
        evaluation.get('feedback_improve', ''),
        evaluation.get('better_example', '')
    ))

    # Update completed question count in parent interview
    conn.execute('''
    UPDATE interviews SET completed_questions = completed_questions + 1 WHERE id = ?
    ''', (interview_id,))
    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "question_number": question_number,
        "evaluation": evaluation
    })

@app.route('/api/interview/finish', methods=['POST'])
def api_interview_finish():
    """Finalize the interview session and calculate summary metrics."""
    data = request.get_json() or {}
    interview_id = data.get('interview_id')
    role = data.get('role', 'Software Developer')
    difficulty = data.get('difficulty', 'Intermediate')

    conn = get_db_connection()
    answers = conn.execute(
        'SELECT * FROM interview_answers WHERE interview_id = ? ORDER BY question_number ASC',
        (interview_id,)
    ).fetchall()

    answers_list = [dict(a) for a in answers]
    summary_report = ai_service.summarize_interview(role, difficulty, answers_list)

    # Update interview record
    conn.execute('''
    UPDATE interviews SET
        overall_score = ?,
        technical_score = ?,
        communication_score = ?,
        confidence_score = ?,
        relevance_score = ?,
        summary = ?,
        strengths_json = ?,
        weaknesses_json = ?,
        recommendations_json = ?
    WHERE id = ?
    ''', (
        summary_report.get('overall_score', 75),
        summary_report.get('technical_score', 75),
        summary_report.get('communication_score', 75),
        summary_report.get('confidence_score', 75),
        summary_report.get('relevance_score', 75),
        summary_report.get('summary', ''),
        json.dumps(summary_report.get('strengths', [])),
        json.dumps(summary_report.get('weaknesses', [])),
        json.dumps(summary_report.get('recommended_topics', [])),
        interview_id
    ))
    conn.commit()
    conn.close()

    return jsonify({
        "interview_id": interview_id,
        "summary": summary_report,
        "answers": answers_list
    })

@app.route('/api/resume/upload', methods=['POST'])
def api_resume_upload():
    """Upload and analyze a PDF resume."""
    target_role = request.form.get('target_role', 'Software Developer')
    
    if 'resume_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume_file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.lower().endswith('.pdf'):
        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex[:8]}_{filename}"
        filepath = os.path.join(Config.UPLOAD_FOLDER, unique_name)
        file.save(filepath)

        # Parse text from PDF
        text = extract_text_from_pdf(filepath)
        analysis = analyze_resume_text(text, target_role=target_role, filename=filename)

        # Save scan result to DB
        scan_id = f"scan-{uuid.uuid4().hex[:8]}"
        conn = get_db_connection()
        conn.execute('''
        INSERT INTO resume_scans (
            id, target_role, filename, ats_score, keyword_match_pct,
            skills_detected_json, missing_keywords_json, formatting_score,
            recommendations_json, full_analysis_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            scan_id, target_role, filename,
            analysis.get('ats_score', 80),
            analysis.get('keyword_match_pct', 75),
            json.dumps(analysis.get('detected_tech_skills', [])),
            json.dumps(analysis.get('missing_keywords', [])),
            analysis.get('formatting_score', 85),
            json.dumps(analysis.get('recommendations', [])),
            json.dumps(analysis)
        ))
        conn.commit()
        conn.close()

        analysis["scan_id"] = scan_id
        return jsonify(analysis)

    return jsonify({"error": "Please upload a valid PDF document."}), 400

@app.route('/api/resume/analyze-text', methods=['POST'])
def api_resume_analyze_text():
    """Analyze pasted resume text."""
    data = request.get_json() or {}
    text = data.get('text', '')
    target_role = data.get('target_role', 'Software Developer')

    analysis = analyze_resume_text(text, target_role=target_role, filename="pasted_resume.txt")
    return jsonify(analysis)

@app.route('/api/skills/gap-analysis', methods=['POST'])
def api_skills_gap_analysis():
    """Perform skill gap analysis for a chosen target career."""
    data = request.get_json() or {}
    target_role = data.get('target_role', 'Software Developer')

    # Get current user skills from DB
    conn = get_db_connection()
    db_skills = conn.execute('SELECT name, proficiency FROM skills').fetchall()
    conn.close()

    user_skills_map = {s['name'].lower(): s['proficiency'] for s in db_skills}

    role_info = ROLE_TAXONOMY.get(target_role, ROLE_TAXONOMY["Software Developer"])
    core_skills = role_info.get("core_skills", [])

    analysis_results = []
    matched_count = 0

    for cs in core_skills:
        name = cs["name"]
        importance = cs["importance"]
        weight = cs["weight"]

        # Check if user has this skill or variant
        user_prof = 0
        for sk_name, prof in user_skills_map.items():
            if any(piece.strip().lower() in name.lower() for piece in sk_name.split()):
                user_prof = max(user_prof, prof)

        if user_prof >= 3:
            matched_count += 1
            gap_status = "Proficient"
            priority = "Low"
        elif user_prof > 0:
            gap_status = "Needs Practice"
            priority = "Medium"
        else:
            gap_status = "Skill Gap"
            priority = "High" if importance == "High" else "Medium"

        analysis_results.append({
            "skill": name,
            "importance": importance,
            "priority": priority,
            "gap_status": gap_status,
            "current_proficiency": user_prof,
            "target_proficiency": 4 if importance == "High" else 3,
            "weight": weight
        })

    readiness_pct = int((matched_count / max(len(core_skills), 1)) * 100)

    return jsonify({
        "target_role": target_role,
        "readiness_percentage": readiness_pct,
        "skills_analyzed": analysis_results,
        "recommended_projects": role_info.get("recommended_projects", []),
        "interview_topics": role_info.get("interview_topics", [])
    })

@app.route('/api/role-matcher/match', methods=['POST'])
def api_role_match():
    """Calculate multi-role matching scores based on skills."""
    data = request.get_json() or {}
    selected_skills = [s.lower() for s in data.get('skills', [])]
    experience_level = data.get('experience_level', 'Fresher / Student')

    results = []
    for role_name, role_data in ROLE_TAXONOMY.items():
        core = role_data.get('core_skills', [])
        total_weight = sum(s.get('weight', 10) for s in core)
        matched_weight = 0
        matched_list = []
        missing_list = []

        for req in core:
            req_name = req['name']
            is_matched = False
            for user_s in selected_skills:
                if user_s in req_name.lower() or req_name.lower() in user_s:
                    is_matched = True
                    break
            if is_matched:
                matched_weight += req.get('weight', 10)
                matched_list.append(req_name)
            else:
                missing_list.append(req_name)

        match_score = int((matched_weight / max(total_weight, 1)) * 100)
        match_score = min(max(match_score, 35), 98)

        results.append({
            "role": role_name,
            "match_percentage": match_score,
            "category": role_data.get('category', 'Engineering'),
            "description": role_data.get('description', ''),
            "matched_skills": matched_list,
            "missing_skills": missing_list,
            "recommended_projects": role_data.get('recommended_projects', []),
            "interview_topics": role_data.get('interview_topics', [])
        })

    results.sort(key=lambda x: x['match_percentage'], reverse=True)
    return jsonify({"matches": results})

@app.route('/api/skills/add', methods=['POST'])
def api_skill_add():
    """Add a new skill to user profile."""
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    category = data.get('category', 'Technical').strip()
    proficiency = int(data.get('proficiency', 3))

    if not name:
        return jsonify({"error": "Skill name is required"}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO skills (name, category, proficiency, is_verified) VALUES (?, ?, ?, 1)',
        (name, category, proficiency)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": f"Skill '{name}' added successfully!"})

@app.route('/api/skills/delete/<int:skill_id>', methods=['DELETE'])
def api_skill_delete(skill_id):
    """Remove a skill from user profile."""
    conn = get_db_connection()
    conn.execute('DELETE FROM skills WHERE id = ?', (skill_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Skill deleted."})

@app.route('/api/certifications/add', methods=['POST'])
def api_cert_add():
    """Add a verified certificate."""
    data = request.get_json() or {}
    title = data.get('title', '').strip()
    issuer = data.get('issuer', '').strip()
    issue_date = data.get('issue_date', '').strip()
    credential_url = data.get('credential_url', Config.DEVELOPER_LINKEDIN).strip()

    if not title:
        return jsonify({"error": "Certificate title is required"}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO certifications (title, issuer, issue_date, credential_url, is_linkedin_synced) VALUES (?, ?, ?, ?, 1)',
        (title, issuer, issue_date, credential_url)
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Certificate added successfully!"})

@app.route('/api/achievements/add', methods=['POST'])
def api_achievement_add():
    """Add a new verified milestone."""
    data = request.get_json() or {}
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    milestone_date = data.get('date', '').strip()
    category = data.get('category', 'Engineering').strip()

    if not title:
        return jsonify({"error": "Achievement title is required"}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO achievements (title, description, milestone_date, category) VALUES (?, ?, ?, ?)',
        (title, description, milestone_date, category)
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Milestone recorded."})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '127.0.0.1')
    print(f"[*] CareerAI server running at http://{host}:{port}")
    app.run(host=host, port=port, debug=True)
