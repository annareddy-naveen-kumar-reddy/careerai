/**
 * CareerAI — Resume Analyzer & ATS Optimizer Controller
 * PDF drag-and-drop, text analysis, and interactive ATS metrics.
 */

document.addEventListener('DOMContentLoaded', () => {
  initDropzone();
  initTextAnalysis();
  initDemoScanBtn();
});

function initDropzone() {
  const dropzone = document.getElementById('resume-dropzone');
  const fileInput = document.getElementById('resume-file-input');
  if (!dropzone || !fileInput) return;

  dropzone.addEventListener('click', () => fileInput.click());

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.add('drag-over');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.remove('drag-over');
    });
  });

  dropzone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length) handleFileUpload(files[0]);
  });

  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) handleFileUpload(e.target.files[0]);
  });
}

async function handleFileUpload(file) {
  if (!file.name.toLowerCase().endsWith('.pdf')) {
    showToast('Please upload a valid PDF document.', 'error');
    return;
  }

  const roleSelect = document.getElementById('target-role-select');
  const targetRole = roleSelect ? roleSelect.value : 'Software Developer';

  const formData = new FormData();
  formData.append('resume_file', file);
  formData.append('target_role', targetRole);

  const statusBox = document.getElementById('upload-status');
  statusBox.style.display = 'block';
  statusBox.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Parsing PDF & calculating ATS score...';

  try {
    const response = await fetch('/api/resume/upload', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    statusBox.style.display = 'none';

    if (response.ok) {
      renderResumeAnalysis(data);
      showToast('Resume analyzed successfully!', 'success');
    } else {
      showToast(data.error || 'Failed to analyze resume.', 'error');
    }
  } catch (err) {
    console.error(err);
    statusBox.style.display = 'none';
    showToast('Server error while parsing resume.', 'error');
  }
}

function initTextAnalysis() {
  const analyzeBtn = document.getElementById('analyze-text-btn');
  if (!analyzeBtn) return;

  analyzeBtn.addEventListener('click', async () => {
    const text = document.getElementById('resume-text-input').value.trim();
    if (text.length < 50) {
      showToast('Please paste at least 50 characters of resume content.', 'error');
      return;
    }

    const roleSelect = document.getElementById('target-role-select');
    const targetRole = roleSelect ? roleSelect.value : 'Software Developer';

    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';

    try {
      const response = await fetch('/api/resume/analyze-text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, target_role: targetRole })
      });
      const data = await response.json();
      renderResumeAnalysis(data);
      showToast('Resume content analyzed successfully!', 'success');
    } catch (err) {
      console.error(err);
      showToast('Error analyzing resume text.', 'error');
    } finally {
      analyzeBtn.disabled = false;
      analyzeBtn.innerHTML = '<i class="fas fa-magic"></i> Analyze Pasted Content';
    }
  });
}

function initDemoScanBtn() {
  const demoBtn = document.getElementById('run-demo-scan-btn');
  if (!demoBtn) return;

  demoBtn.addEventListener('click', async () => {
    demoBtn.disabled = true;
    demoBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating Demo Analysis...';

    try {
      const roleSelect = document.getElementById('target-role-select');
      const targetRole = roleSelect ? roleSelect.value : 'Software Developer';

      const res = await fetch('/api/resume/analyze-text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: '', target_role: targetRole })
      });
      const data = await res.json();
      renderResumeAnalysis(data);
      showToast('Loaded demo resume analysis.', 'info');
    } catch (err) {
      console.error(err);
    } finally {
      demoBtn.disabled = false;
      demoBtn.innerHTML = '<i class="fas fa-flask"></i> Try Sample Analysis';
    }
  });
}

function renderResumeAnalysis(data) {
  const resultContainer = document.getElementById('resume-analysis-results');
  resultContainer.style.display = 'block';

  // ATS Score
  document.getElementById('ats-score-display').textContent = data.ats_score;
  document.getElementById('keyword-match-display').textContent = `${data.keyword_match_pct}%`;
  document.getElementById('keyword-match-bar').style.width = `${data.keyword_match_pct}%`;

  document.getElementById('format-score-display').textContent = `${data.formatting_score}%`;
  document.getElementById('format-score-bar').style.width = `${data.formatting_score}%`;

  // Tech Skills
  const techContainer = document.getElementById('detected-tech-skills');
  techContainer.innerHTML = '';
  (data.detected_tech_skills || []).forEach(s => {
    const pill = document.createElement('span');
    pill.className = 'skill-pill tech';
    pill.innerHTML = `<i class="fas fa-code"></i> ${s}`;
    techContainer.appendChild(pill);
  });

  // Soft Skills
  const softContainer = document.getElementById('detected-soft-skills');
  softContainer.innerHTML = '';
  (data.detected_soft_skills || []).forEach(s => {
    const pill = document.createElement('span');
    pill.className = 'skill-pill soft';
    pill.innerHTML = `<i class="fas fa-user-check"></i> ${s}`;
    softContainer.appendChild(pill);
  });

  // Missing Keywords
  const missingContainer = document.getElementById('missing-keywords');
  missingContainer.innerHTML = '';
  (data.missing_keywords || []).forEach(s => {
    const pill = document.createElement('span');
    pill.className = 'skill-pill missing';
    pill.innerHTML = `<i class="fas fa-plus"></i> ${s}`;
    missingContainer.appendChild(pill);
  });

  // Checklist
  const sections = data.sections_detected || {};
  updateChecklistItem('chk-education', sections.education);
  updateChecklistItem('chk-skills', sections.skills);
  updateChecklistItem('chk-projects', sections.projects);
  updateChecklistItem('chk-experience', sections.experience);
  updateChecklistItem('chk-certifications', sections.certifications);

  // Recommendations
  const recList = document.getElementById('resume-recommendations');
  recList.innerHTML = '';
  (data.recommendations || []).forEach(r => {
    const li = document.createElement('li');
    li.style.marginBottom = '0.6rem';
    li.innerHTML = `<i class="fas fa-lightbulb" style="color: var(--accent-cyan)"></i> ${r}`;
    recList.appendChild(li);
  });

  resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function updateChecklistItem(id, isPresent) {
  const el = document.getElementById(id);
  if (!el) return;
  el.className = `checklist-item ${isPresent ? 'detected' : 'missing'}`;
  el.querySelector('i').className = `fas ${isPresent ? 'fa-check-circle' : 'fa-times-circle'}`;
}
