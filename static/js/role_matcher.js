/**
 * CareerAI — Skill Gap Analyzer & Job Role Matcher Controller
 * Dual Client & Server Engine for 100% GitHub Pages & Static Site Compatibility.
 */

// Client-Side Taxonomy for Offline / GitHub Pages Gap Analysis
const CLIENT_GAP_DATA = {
  "Software Developer": {
    readiness_percentage: 84,
    skills_analyzed: [
      { skill: "Data Structures & Algorithms", importance: "High", priority: "High", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Python / Java / C++", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Object-Oriented Programming (OOP)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "SQL & Relational Databases", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "RESTful API Design", importance: "Medium", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Git & Version Control", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "System Design & Scalability", importance: "Medium", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 }
    ],
    recommended_projects: [
      "Full-Stack Web App with REST API & SQLite/PostgreSQL",
      "Multi-threaded Task Queue or In-Memory Cache System",
      "Algorithmic Data Analyzer with Visual Benchmarks"
    ],
    interview_topics: [
      "Time & Space Complexity Analysis (Big O Notation)",
      "OOP Principles (Encapsulation, Polymorphism, Inheritance, Abstraction)",
      "Database Indexing, Normalization & ACID Transactions",
      "API Authentication (JWT/OAuth) and Error Handling",
      "Concurrency, Threads, and Process Management"
    ]
  },
  "Python Developer": {
    readiness_percentage: 92,
    skills_analyzed: [
      { skill: "Python (Advanced OOP & Metaprogramming)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Flask / FastAPI / Django", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "SQL & ORMs (SQLAlchemy)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Asyncio & Multiprocessing", importance: "Medium", priority: "Medium", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Unit Testing & Pytest", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Git & CI/CD", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Docker Basics", importance: "Low", priority: "High", gap_status: "Skill Gap", current_proficiency: 2 }
    ],
    recommended_projects: [
      "Microservice REST API with Flask/FastAPI & Token Authentication",
      "Automated Web Scraping and Data Pipeline with Celery",
      "Facial Recognition or OpenCV Vision Processing Service"
    ],
    interview_topics: [
      "Python Memory Management & Global Interpreter Lock (GIL)",
      "Generators, Iterators, and List Comprehensions",
      "Decorators, Context Managers (with statement), and Dunder methods",
      "Flask vs Django architectural trade-offs",
      "Database Connection Pooling & Query Optimization"
    ]
  },
  "Web Developer": {
    readiness_percentage: 88,
    skills_analyzed: [
      { skill: "HTML5 & Modern CSS3 (Flexbox/Grid)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "JavaScript (ES6+) & DOM APIs", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Responsive Design & Mobile-First UX", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Backend Integration (Flask/Node.js)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "REST APIs & Fetch/Axios", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Web Performance & Accessibility (a11y)", importance: "Medium", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Git & Web Deployment", importance: "Low", priority: "Low", gap_status: "Proficient", current_proficiency: 5 }
    ],
    recommended_projects: [
      "Dynamic SaaS Dashboard with Dark/Light Themes and Glassmorphism",
      "E-Commerce Cart or Booking Engine with Real-Time Validation",
      "Interactive Single Page Application (SPA) with Flask REST Backend"
    ],
    interview_topics: [
      "CSS Box Model, Flexbox vs CSS Grid, and Media Queries",
      "JavaScript Event Loop, Closures, Promises, and Async/Await",
      "Browser Rendering Lifecycle and DOM Manipulation Performance",
      "Cross-Origin Resource Sharing (CORS) & Security Headers",
      "Progressive Enhancement and Semantic Web Standards"
    ]
  },
  "Data Analyst": {
    readiness_percentage: 78,
    skills_analyzed: [
      { skill: "SQL (Complex Joins & Window Functions)", importance: "High", priority: "High", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Python (Pandas, NumPy)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Data Visualization (Matplotlib, Seaborn, PowerBI)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Exploratory Data Analysis (EDA)", importance: "High", priority: "High", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Statistical Analysis & Probability", importance: "Medium", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Excel / Google Sheets Advanced", importance: "Low", priority: "Low", gap_status: "Proficient", current_proficiency: 4 }
    ],
    recommended_projects: [
      "End-to-End Sales & Churn Analytics Dashboard with Python & SQL",
      "IoT Environmental Sensor Trend and Outlier Analysis",
      "Customer Segmentation Analysis with Clustering Visualization"
    ],
    interview_topics: [
      "SQL Window Functions (ROW_NUMBER, RANK, LEAD, LAG)",
      "Handling Missing Values, Outliers, and Data Imputation",
      "Correlation vs Causation and Hypothesis Testing",
      "Data Storytelling and Executive KPI Presentation",
      "ETL Pipelines and Data Cleansing Strategies"
    ]
  },
  "AI/ML Beginner": {
    readiness_percentage: 82,
    skills_analyzed: [
      { skill: "Python for Data Science (NumPy, Scikit-Learn)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Supervised & Unsupervised Learning Concepts", importance: "High", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Computer Vision Basics (OpenCV)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Model Evaluation Metrics (Precision, Recall, F1, ROC)", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Data Preprocessing & Feature Engineering", importance: "Medium", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Neural Networks & Deep Learning Foundations", importance: "Medium", priority: "High", gap_status: "Skill Gap", current_proficiency: 2 }
    ],
    recommended_projects: [
      "OpenCV Facial Recognition Attendance System with Anti-Spoofing",
      "Predictive Anomaly Detection on IoT Telemetry with Scikit-Learn",
      "Text Classification or Resume Skill Extraction NLP Pipeline"
    ],
    interview_topics: [
      "Bias-Variance Tradeoff and Overfitting Prevention",
      "Supervised vs Unsupervised vs Reinforcement Learning",
      "Confusion Matrix, Precision, Recall, and Accuracy paradox",
      "Image Processing Kernels, Edge Detection, and Feature Extraction in OpenCV",
      "Gradient Descent and Loss Functions"
    ]
  },
  "ECE Engineer": {
    readiness_percentage: 90,
    skills_analyzed: [
      { skill: "Microcontrollers & Embedded C (ESP32 / Arduino / ARM)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "IoT Protocols (MQTT, HTTP, WebSockets, UART, I2C, SPI)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Digital & Analog Electronics Principles", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Sensor Interfacing & Signal Acquisition", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Digital Twin & Real-Time Monitoring Systems", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "Python for Hardware Telemetry & Automation", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 5 }
    ],
    recommended_projects: [
      "SmartLabTwinAI: Digital Twin with ESP32, Temp/Voltage Monitoring & Anomaly Detection",
      "Industrial Automated Motor Control with IoT Telemetry and MQTT",
      "Real-Time Wireless Sensor Network with Power Management"
    ],
    interview_topics: [
      "I2C vs SPI vs UART Communication Protocols: Clocking, Speeds, and Bus Topology",
      "Analog-to-Digital Conversion (ADC), Sampling Rate, and Nyquist Theorem",
      "ESP32 Wi-Fi/Bluetooth Architecture and Power Sleep Modes",
      "Digital Twin Architecture: Virtual Models, Sensor Telemetry, and Predictive Maintenance",
      "Feedback Amplifiers, Op-Amp Circuits, and Signal Filtering"
    ]
  },
  "Custom Role": {
    readiness_percentage: 85,
    skills_analyzed: [
      { skill: "Problem Solving & Algorithmic Thinking", importance: "High", priority: "Medium", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Core Programming (Python / JS / C++)", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 5 },
      { skill: "System Architecture & Design", importance: "High", priority: "High", gap_status: "Needs Practice", current_proficiency: 3 },
      { skill: "Database & Storage Management", importance: "Medium", priority: "Low", gap_status: "Proficient", current_proficiency: 4 },
      { skill: "Technical Communication & Collaboration", importance: "High", priority: "Low", gap_status: "Proficient", current_proficiency: 4 }
    ],
    recommended_projects: [
      "End-to-End Applied Engineering Application",
      "Integrated Hardware-Software Telemetry System",
      "AI-Assisted Workflow Automation Platform"
    ],
    interview_topics: [
      "Software Development Lifecycle (SDLC) and Agile Methodologies",
      "Modular Code Architecture and Clean Code Practices",
      "Troubleshooting, Debugging, and Root Cause Analysis",
      "Technical Trade-off Decisions and Scalability Planning"
    ]
  }
};

const CLIENT_ROLE_DEFINITIONS = [
  {
    role: "Python Developer",
    category: "Backend & Systems",
    description: "Builds scalable APIs, server-side business logic, automation scripts, and database integrations.",
    required_skills: ["Python", "Flask", "SQL", "Git", "REST APIs", "OpenCV"],
    optional_skills: ["Docker", "Linux", "Asyncio", "Celery"]
  },
  {
    role: "Full Stack Web Developer",
    category: "Full Stack Development",
    description: "Constructs end-to-end web applications with modern HTML5/CSS3 interfaces and robust backend logic.",
    required_skills: ["JavaScript", "HTML5", "CSS3", "Python", "SQL", "Git"],
    optional_skills: ["React", "Flask", "REST APIs", "Node.js"]
  },
  {
    role: "Embedded & IoT Engineer",
    category: "Hardware & Firmware",
    description: "Programs microcontrollers, implements wireless communication protocols, and streams telemetry.",
    required_skills: ["Embedded C", "ESP32", "Arduino", "IoT Protocols", "Sensors"],
    optional_skills: ["Python", "Digital Twin", "MQTT", "Circuit Design"]
  },
  {
    role: "Data Analyst",
    category: "Data & Insights",
    description: "Extracts business intelligence, writes complex SQL queries, and builds interactive telemetry dashboards.",
    required_skills: ["SQL", "Python", "Pandas", "Data Visualization", "Google Sheets API"],
    optional_skills: ["PowerBI", "Statistics", "EDA", "Machine Learning"]
  },
  {
    role: "AI / Computer Vision Engineer",
    category: "Artificial Intelligence",
    description: "Designs machine learning models, applies OpenCV image recognition algorithms, and deploys smart edge inference.",
    required_skills: ["Python", "OpenCV", "Machine Learning", "Data Structures"],
    optional_skills: ["Deep Learning", "TensorFlow", "PyTorch", "Flask"]
  },
  {
    role: "Software Developer (General)",
    category: "Core Software Engineering",
    description: "Develops modular algorithms, designs clean software architecture, and manages production git workflows.",
    required_skills: ["Python", "JavaScript", "SQL", "Git", "Data Structures"],
    optional_skills: ["C++", "System Design", "Linux", "REST APIs"]
  }
];

document.addEventListener('DOMContentLoaded', () => {
  initSkillGapCalculator();
  initRoleMatcherCalculator();
});

/* ===================================================================
   SKILL GAP ANALYZER
   =================================================================== */
function initSkillGapCalculator() {
  const roleSelect = document.getElementById('gap-target-role');
  if (!roleSelect) return;

  roleSelect.addEventListener('change', () => {
    fetchSkillGapAnalysis(roleSelect.value);
  });

  // Initial load
  fetchSkillGapAnalysis(roleSelect.value || 'Software Developer');
}

async function fetchSkillGapAnalysis(role) {
  const container = document.getElementById('skill-gap-table-body');
  if (!container) return;

  container.innerHTML = '<tr><td colspan="5" style="text-align:center; padding: 2rem;"><i class="fas fa-spinner fa-spin"></i> Calculating skill alignment...</td></tr>';

  let data = null;
  const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');

  if (isLocalBackend) {
    try {
      const res = await fetch('/api/skills/gap-analysis', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ target_role: role })
      });
      if (res.ok) {
        data = await res.json();
      }
    } catch (err) {
      console.log('Using client skill gap data.');
    }
  }

  // Fallback to client data
  if (!data) {
    data = CLIENT_GAP_DATA[role] || CLIENT_GAP_DATA["Software Developer"];
  }

  renderSkillGapResults(data);
}

function renderSkillGapResults(data) {
  const tbody = document.getElementById('skill-gap-table-body');
  const readinessText = document.getElementById('gap-readiness-val');
  const readinessBar = document.getElementById('gap-readiness-bar');

  if (readinessText) readinessText.textContent = `${data.readiness_percentage}%`;
  if (readinessBar) readinessBar.style.width = `${data.readiness_percentage}%`;

  if (!tbody) return;
  tbody.innerHTML = '';

  (data.skills_analyzed || []).forEach(item => {
    const tr = document.createElement('tr');
    tr.style.borderBottom = '1px solid var(--border-subtle)';

    const priorityBadge = item.priority === 'High' 
      ? '<span class="badge badge-amber">High Priority</span>'
      : (item.priority === 'Medium' ? '<span class="badge badge-cyan">Medium</span>' : '<span class="badge badge-emerald">On Track</span>');

    const statusBadge = item.gap_status === 'Proficient'
      ? '<span style="color: var(--accent-emerald); font-weight: 600;"><i class="fas fa-check-circle"></i> Proficient</span>'
      : (item.gap_status === 'Needs Practice' 
        ? '<span style="color: var(--accent-amber); font-weight: 600;"><i class="fas fa-wrench"></i> Needs Practice</span>'
        : '<span style="color: var(--accent-rose); font-weight: 600;"><i class="fas fa-arrow-up"></i> Skill Gap</span>');

    tr.innerHTML = `
      <td style="padding: 1rem 0.75rem; font-weight: 600; color: var(--text-primary);">${item.skill}</td>
      <td style="padding: 1rem 0.75rem;">${item.importance}</td>
      <td style="padding: 1rem 0.75rem;">${priorityBadge}</td>
      <td style="padding: 1rem 0.75rem;">${statusBadge}</td>
      <td style="padding: 1rem 0.75rem;">
        <div class="progress-wrapper" style="height: 6px; width: 100px;">
          <div class="progress-fill ${item.current_proficiency >= 3 ? 'progress-fill-emerald' : ''}" style="width: ${(item.current_proficiency / 5) * 100}%"></div>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });

  // Recommended Projects
  const projList = document.getElementById('gap-recommended-projects');
  if (projList) {
    projList.innerHTML = '';
    (data.recommended_projects || []).forEach(p => {
      const li = document.createElement('li');
      li.style.marginBottom = '0.5rem';
      li.innerHTML = `<i class="fas fa-project-diagram" style="color: var(--accent-cyan)"></i> ${p}`;
      projList.appendChild(li);
    });
  }

  // Interview Topics
  const topicList = document.getElementById('gap-interview-topics');
  if (topicList) {
    topicList.innerHTML = '';
    (data.interview_topics || []).forEach(t => {
      const li = document.createElement('li');
      li.style.marginBottom = '0.5rem';
      li.innerHTML = `<i class="fas fa-book" style="color: var(--accent-emerald)"></i> ${t}`;
      topicList.appendChild(li);
    });
  }
}

/* ===================================================================
   JOB ROLE MATCHER
   =================================================================== */
function initRoleMatcherCalculator() {
  const calcBtn = document.getElementById('calculate-match-btn');
  if (!calcBtn) return;

  calcBtn.addEventListener('click', async () => {
    const selectedSkills = [];
    document.querySelectorAll('.matcher-skill-checkbox:checked').forEach(chk => {
      selectedSkills.push(chk.value);
    });

    if (selectedSkills.length === 0) {
      showToast('Please select at least 1 skill from the checklist.', 'error');
      return;
    }

    const expSelect = document.getElementById('matcher-exp-select');
    const expLevel = expSelect ? expSelect.value : 'Fresher';

    calcBtn.disabled = true;
    calcBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Calculating Fit...';

    let matches = null;
    const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');

    if (isLocalBackend) {
      try {
        const res = await fetch('/api/role-matcher/match', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ skills: selectedSkills, experience_level: expLevel })
        });
        if (res.ok) {
          const data = await res.json();
          matches = data.matches;
        }
      } catch (err) {
        console.log('Using client role matching engine.');
      }
    }

    // Client-Side Calculation Fallback
    if (!matches) {
      matches = calculateClientRoleMatches(selectedSkills, expLevel);
    }

    renderRoleMatchCards(matches);
    showToast('Role matching calculated successfully!', 'success');

    calcBtn.disabled = false;
    calcBtn.innerHTML = '<i class="fas fa-calculator"></i> Match My Profile';
  });
}

function calculateClientRoleMatches(userSkills, expLevel) {
  const userSkillsLower = userSkills.map(s => s.toLowerCase());

  const results = CLIENT_ROLE_DEFINITIONS.map(def => {
    const matched = [];
    const missing = [];

    def.required_skills.forEach(req => {
      const isMatched = userSkillsLower.some(us => us.includes(req.toLowerCase()) || req.toLowerCase().includes(us));
      if (isMatched) {
        matched.push(req);
      } else {
        missing.push(req);
      }
    });

    let matchPct = Math.round((matched.length / def.required_skills.length) * 100);
    if (expLevel === '1-2 Years') matchPct = Math.min(matchPct + 5, 98);
    else if (expLevel === '3+ Years') matchPct = Math.min(matchPct + 8, 98);

    return {
      role: def.role,
      category: def.category,
      description: def.description,
      match_percentage: matchPct,
      matched_skills: matched,
      missing_skills: missing
    };
  });

  // Sort descending by match percentage
  results.sort((a, b) => b.match_percentage - a.match_percentage);
  return results;
}

function renderRoleMatchCards(matches) {
  const container = document.getElementById('role-matches-grid');
  if (!container) return;

  container.innerHTML = '';

  (matches || []).forEach((m) => {
    const card = document.createElement('div');
    card.className = 'glass-card hover-lift';
    card.style.display = 'flex';
    card.style.flexDirection = 'column';
    card.style.gap = '1rem';

    const matchColor = m.match_percentage >= 75 ? 'var(--accent-emerald)' : (m.match_percentage >= 50 ? 'var(--accent-cyan)' : 'var(--accent-amber)');

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <span class="badge badge-cyan" style="margin-bottom: 0.4rem;">${m.category}</span>
          <h3 style="font-size: 1.25rem;">${m.role}</h3>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 1.85rem; font-weight: 800; color: ${matchColor};">${m.match_percentage}%</span>
          <div style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase;">Match Score</div>
        </div>
      </div>

      <p style="font-size: 0.88rem;">${m.description}</p>

      <div class="progress-wrapper" style="height: 6px;">
        <div class="progress-fill" style="width: ${m.match_percentage}%; background: ${matchColor};"></div>
      </div>

      <div>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-emerald); margin-bottom: 0.4rem; text-transform: uppercase;">
          <i class="fas fa-check-circle"></i> Matching Skills (${m.matched_skills.length})
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">
          ${m.matched_skills.map(s => `<span class="skill-pill tech" style="font-size: 0.75rem;">${s}</span>`).join('')}
        </div>
      </div>

      ${m.missing_skills.length ? `
      <div>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-rose); margin-bottom: 0.4rem; text-transform: uppercase;">
          <i class="fas fa-exclamation-circle"></i> Recommended to Learn
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">
          ${m.missing_skills.slice(0, 3).map(s => `<span class="skill-pill missing" style="font-size: 0.75rem;">${s}</span>`).join('')}
        </div>
      </div>
      ` : ''}

      <div style="margin-top: auto; padding-top: 0.5rem;">
        <a href="interview.html" class="btn btn-secondary btn-sm" style="width: 100%;">
          <i class="fas fa-microphone"></i> Practice ${m.role} Interview
        </a>
      </div>
    `;

    container.appendChild(card);
  });

  container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
